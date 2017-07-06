# -*- coding: utf-8 -*-

from plugins.common.base_messenger import BaseMessenger
from plugins.common.output_level_manager import OutputLevelManager

class TaskMessenger(BaseMessenger):
    """タスク管理に関するコマンドの管理クラス"""

    __OUTPUT_LEVEL = 2
    """
    自クラスのメッセージ出力レベル
    このクラスのみ例外的に0とし常に出力する
    """

    __SETTASK_USAGE = "Usage:taskset タスク名 [-u 担当者] [-p 進捗]"
    """settaskコマンドのUsage"""

    def __init__(self):
        """コンストラクタ"""
        BaseMessenger.__init__(self, self.__OUTPUT_LEVEL)

    def exec_set(self, message):
        """
        タスクル設定コマンド実行
        param message:受け取ったメッセージの文字列
        return:botが応答するメッセージ
        """

        # メッセージレベル出力可能チェック
        if not self.can_output_level():
            return ""

        # コマンドチェック
        errmsg = self.get_errmsg_about_arg(message)

        # エラーがある場合はエラーメッセージを出力
        elif errmsg:
            return errmsg

        OutputLevelManager.set_output_level(self.setlevel)

        return "設定しました" % (self.setlevel)

    def get_errmsg_about_arg(self, msg):
        """
        入力コマンドチェック処理
        param msg:受け取ったメッセージの文字列
        return:エラーありの場合はエラーメッセージ
               エラーなしの場合は空文字
        """

        args = msg.split()

        if len(args) < 2:
             return "コマンドが不正です\n" + self.__SETTASK_USAGE

        level = int(args[1])

        if level < 0 or level > 10:
            return "出力レベルは0〜10の数字を指定してください\n" + self.__SETLEVEL_USAGE

        self.setlevel = level
        return ""
