#! python 3
# -*- coding: utf-8 -*-
"""說明指令。工具列只呼叫既有的 R2B、R2O、R2M 指令，本身不同步。"""

MESSAGE = (
    "LoopFlow R2X is a shared toolbar. "
    "Its buttons call Rhino to Blender Sync, Rhino to Octane Sync, and Rhino to MEP Sync. "
    "Install those products separately. This package does not sync anything by itself."
)

_started = False


def _run():
    global _started
    if _started:
        return
    _started = True
    print(MESSAGE)


def RunCommand(is_interactive):
    _run()


_run()
