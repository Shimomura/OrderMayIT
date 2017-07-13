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

        if(self.exist_memo(num)):
            raise Exception("登録済みのメモ番号")

        # TODO タイムゾーンを考慮
        date = datetime.datetime.today()
        memo = MemoInfo(num, content, date)
        self.memo_list.append(memo)

    def del_memo(self, num):
        """メモリストからメモを削除します"""

        if not self.exist_memo(num):
            raise Exception("指定メモは存在しません")

        target = self.get_memo(num)

        self.memo_list.remove(target)

        # メモ番号を採番、削除のタイミングのみ採番し直せばメモ番号は一意となる想定
        self.memo_list = sorted(self.memo_list,key = lambda l:int(l.memo_No))
        for memo in self.memo_list:
            memo.memo_No = self.memo_list.index(memo) + 1
        # パフォーマンスはよくないけど、そんなにたくさんメモ残さないよね・・・？

    def get_memo(self, num):
        """メモリスト内から一致するメモNoのメモを取得します"""

        if num is str and not num.isdigit():
            return None

        num_int = int(num)
        target = list(filter(lambda m:m.memo_No == num_int, self.memo_list))

        if target:
            return target[0]

        return None

    def exist_memo(self, num):
        """メモがメモリストに存在するか取得します"""

        target = self.get_memo(num)
        if target:
            return True
        return False
