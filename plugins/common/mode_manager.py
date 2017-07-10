# -*- coding: utf-8 -*-

from enum import Enum

class ProcessModeEnum(Enum):
    Normal   = "通常モード"
    MemoSave = "メモ保存"
    MemoDisp = "メモ表示"
    MemoDel  = "メモ削除"

class ModeManager:
    now_mode = ProcessModeEnum.Normal
