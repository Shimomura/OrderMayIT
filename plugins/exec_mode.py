# -*- coding: utf-8 -*-

from plugins.common.mode_manager import ModeManager
from plugins.common.mode_manager import ProcessModeEnum
from plugins.memo.memo_messenger import MemoMessenger

def exec_mode(message):

    mode = ModeManager.now_mode

    if mode is ProcessModeEnum.MemoSave:
        ModeManager.now_mode = ProcessModeEnum.Normal
        messenger = MemoMessenger()
        return messenger.exec_set(message)

    elif mode is ProcessModeEnum.MemoDisp:
        ModeManager.now_mode = ProcessModeEnum.Normal
        messenger = MemoMessenger()
        return messenger.exec_disp(message)

    elif mode is ProcessModeEnum.MemoDel:
        ModeManager.now_mode = ProcessModeEnum.Normal
        messenger = MemoMessenger()
        return messenger.exec_del(message)
