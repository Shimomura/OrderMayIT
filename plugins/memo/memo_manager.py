# -*- coding: utf-8 -*-

import datetime
from plugins.memo.memo_info import MemoInfo

class MemoManager(object):
    """メモ管理クラス"""

    __instance = None
    """自クラスのインスタンス"""

    memo_list = []

    def __new__(clsObj, *args, **kwargs):
        """シングルトンとする"""
        if not hasattr(clsObj, "__instance__"):
            clsObj.__instance__ = super(MemoManager, clsObj).__new__(clsObj, *args, **kwargs)
        return clsObj.__instance__

    def __init__(self, *args, **kwargs):
        """コンストラクタ"""
        pass

    def add_memo(self, content):
        """メモリストにメモを追加します"""

        num = len(self.memo_list) + 1
        # TODO タイムゾーンを考慮
        date = datetime.datetime.today()
        memo = MemoInfo(num, content, date)
        self.memo_list.append(memo)

    def del_task(self, num):
        """メモリストからメモを削除します"""

        if not self.exist_memo(num):
            raise Exception("指定メモは存在しません")

        target = self.get_memo(num)

        self.memo_list.remove(target)

    def get_memo(self, num):
        """メモリスト内から一致するメモNoのメモを取得します"""

        if not num.isdigit():
            return None

        num_int = int(num)
        target = list(filter(lambda m:m.memo_No == num_int, self.memo_list))

        if target:
            return target[0]

        return None

    def exist_memo(self, num):
        """メモがメモリストに存在するか取得します"""

        target = list(filter(lambda m:m.memo_No == num, self.memo_list))
        if target:
            return True
        return False
