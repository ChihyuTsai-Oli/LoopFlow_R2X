#Requires -Version 5.1
# R2X: rhproj -> rhp -> stage the shared toolbar -> yak
$ErrorActionPreference = "Stop"

$Spike = $PSScriptRoot
$RepoRoot = (Resolve-Path (Join-Path $Spike "..")).Path
$Toolbar = Join-Path $RepoRoot "toolbar"
$Rhproj = Join-Path $Spike "loopflow-R2X.rhproj"
$RhinoCode = "C:\Program Files\Rhino 8\System\RhinoCode.exe"
$Yak = "C:\Program Files\Rhino 8\System\yak.exe"

if (-not (Test-Path -LiteralPath $Rhproj)) {
    Write-Host "Missing $Rhproj"
    exit 1
}
if (-not (Test-Path -LiteralPath $RhinoCode)) {
    Write-Host "RhinoCode.exe not found: $RhinoCode"
    exit 1
}

Write-Host "Building $Rhproj"
& $RhinoCode project build $Rhproj
if ($LASTEXITCODE -ne 0) {
    throw "RhinoCode project build failed: $LASTEXITCODE"
}

$AutoRuiDir = Join-Path $Spike "build\rh8"
if (Test-Path -LiteralPath $AutoRuiDir) {
    Get-ChildItem -LiteralPath $AutoRuiDir -Filter "*.rui" -File -ErrorAction SilentlyContinue | ForEach-Object {
        Write-Host "Removing auto-generated RUI $($_.Name)"
        Remove-Item -LiteralPath $_.FullName -Force
    }
}

$Stage = Join-Path $Spike "build\yak-stage"
if (Test-Path -LiteralPath $Stage) {
    Remove-Item -LiteralPath $Stage -Recurse -Force
}
New-Item -ItemType Directory -Path $Stage | Out-Null
Copy-Item -LiteralPath (Join-Path $Spike "manifest.yml") -Destination (Join-Path $Stage "manifest.yml")

$Icon = Join-Path $Spike "icon.png"
if (-not (Test-Path -LiteralPath $Icon)) {
    throw "Missing icon.png"
}
Copy-Item -LiteralPath $Icon -Destination (Join-Path $Stage "icon.png") -Force
Write-Host "Staged icon.png"

$StagedRhp = Get-ChildItem -LiteralPath (Join-Path $Spike "build\rh8") -Filter "*.rhp" -File -ErrorAction SilentlyContinue | Select-Object -First 1
if ($null -eq $StagedRhp) {
    throw "RhinoCode did not produce an .rhp"
}
Copy-Item -LiteralPath $StagedRhp.FullName -Destination (Join-Path $Stage $StagedRhp.Name) -Force
Write-Host "Staged $($StagedRhp.Name)"

$ProductRui = Join-Path $Toolbar "LoopFlow_R2X.rui"
if (-not (Test-Path -LiteralPath $ProductRui)) {
    throw "Missing $ProductRui"
}
$RuiName = "$($StagedRhp.Name)".Replace(".rhp", ".rui")
if ($RuiName -ne "LoopFlow R2X.rui") {
    throw "product RUI name is [$RuiName]"
}
$RuiDest = Join-Path $Stage $RuiName
Copy-Item -LiteralPath $ProductRui -Destination $RuiDest -Force
if (-not (Test-Path -LiteralPath $RuiDest)) {
    throw "product RUI was not staged as $RuiName"
}
Write-Host "Staged product RUI $RuiName"

if (-not (Test-Path -LiteralPath $Yak)) {
    Write-Host "yak.exe not found: $Yak"
    exit 1
}

Get-ChildItem -LiteralPath $Spike -Filter "*.yak" -File -ErrorAction SilentlyContinue | Remove-Item -Force

Push-Location $Stage
try {
    & $Yak build
    if ($LASTEXITCODE -ne 0) {
        throw "yak build failed: $LASTEXITCODE"
    }
    Get-ChildItem -LiteralPath $Stage -Filter "*.yak" -File | ForEach-Object {
        $DestYak = Join-Path $Spike $_.Name
        Copy-Item -LiteralPath $_.FullName -Destination $DestYak -Force
        Write-Host "Wrote $DestYak"
    }
} finally {
    Pop-Location
}

Write-Host "Done."
