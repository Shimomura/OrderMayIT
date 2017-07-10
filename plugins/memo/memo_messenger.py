# -*- coding: utf-8 -*-

from plugins.common.base_messenger import BaseMessenger
from plugins.common.output_level_manager import OutputLevelManager
from plugins.common import common_utill
from plugins.common.invalid_command_exception import InvalidCommandException
from plugins.memo.memo_manager import MemoManager
from plugins.memo.memo_info import MemoInfo

class MemoMessenger(BaseMessenger):
    """メモ管理に関するコマンドの管理クラス"""

    __OUTPUT_LEVEL = 2
    """
    自クラスのメッセージ出力レベル
    このクラスのみ例外的に0とし常に出力する
    """

    def __init__(self):
        """コンストラクタ"""
        BaseMessenger.__init__(self, self.__OUTPUT_LEVEL)

    def exec_list(self):
        """
        メモリスト表示
        return:botが応答するメッセージ
        """

        # メッセージレベル出力可能チェック
        if not self.can_output_level():
            return ""

        manager = MemoManager()
        memos = manager.memo_list
        print("メモ数" + str(len(manager.memo_list)))

        msg = ""

        for memo in memos:
            msg += "No." + str(memo.memo_No) + "  " \
                 + memo.memo_contents[:6] + "  " \
                 + memo.memo_date.strftime("%Y/%m/%d %H:%M:%S") + "\n"

        return msg

    def exec_disp(self, num):
        """
        メモ表示
        param num:表示するメモNo
        return:botが応答するメッセージ
        """

        # メッセージレベル出力可能チェック
        if not self.can_output_level():
            return ""

        manager = MemoManager()
        target = manager.get_memo(num)

        if not target:
            return "該当するメモはありません。"

        return "No." + str(target.memo_No) + "\n" \
             + target.memo_date.strftime("%Y/%m/%d %H:%M:%S") + "\n" \
             + target.memo_contents

    def exec_set(self, message):
        """
        メモ保存実行
        param message:受け取ったメッセージの文字列
        return:botが応答するメッセージ
        """

        # メッセージレベル出力可能チェック
        if not self.can_output_level():
            return ""

        manager = MemoManager()
        manager.add_memo(message)
        print("メモ数" + str(len(manager.memo_list)))

        return "メモしました。"
