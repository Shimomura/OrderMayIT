# -*- coding: utf-8 -*-

from plugins.common.base_messenger import BaseMessenger
from plugins.common.output_level_manager import OutputLevelManager
from plugins.common import common_utill
from plugins.common.invalid_command_exception import InvalidCommandException
from plugins.task.task_manager import TaskManager
from plugins.task.task_info import TaskInfo

class TaskMessenger(BaseMessenger):
    """タスク管理に関するコマンドの管理クラス"""

    __OUTPUT_LEVEL = 2
    """
    自クラスのメッセージ出力レベル
    このクラスのみ例外的に0とし常に出力する
    """

    __SETTASK_USAGE = "Usage:settask タスク名 [-u 担当者] [-p 進捗]"
    """settaskコマンドのUsage"""

    __OPTION_PERSON = "-u"
    """担当者オプション"""

    __OPTION_PROGRESS = "-p"
    """進捗オプション"""

    __OPTION_NAME = "-n"
    """タスク名オプション"""

    def __init__(self):
        """コンストラクタ"""
        BaseMessenger.__init__(self, self.__OUTPUT_LEVEL)

    def exec_list(self, message):
        """
        タスク表示コマンド実行
        param message:受け取ったメッセージの文字列
        return:botが応答するメッセージ
        """

        # メッセージレベル出力可能チェック
        if not self.can_output_level():
            return ""

        # コマンドチェック
        errmsg = self.get_errmsg_list_arg(message)

        # エラーがある場合はエラーメッセージを出力
        if errmsg:
            return errmsg

        args = message.split()

        name = ""
        person = ""
        progress = ""

        if len(args) > 1:
            opt_maps = common_utill.split_options(args[1:])
            name = (opt_maps[TaskMessenger.__OPTION_NAME])[0] if TaskMessenger.__OPTION_NAME in opt_maps else ""
            person = (opt_maps[TaskMessenger.__OPTION_PERSON])[0] if TaskMessenger.__OPTION_PERSON in opt_maps else ""
            progress = (opt_maps[TaskMessenger.__OPTION_PROGRESS])[0] if TaskMessenger.__OPTION_PROGRESS in opt_maps else ""

        manager = TaskManager()
        targets = manager.get_task(name, person, progress)

        if not targets:
            return "該当するタスクが存在しません。"

        msg = ""

        for target in targets:
            msg += target.task_name + "  担当：" + target.task_person + "  進捗：" + target.task_progress + "%\n"

        return msg

    def exec_set(self, message):
        """
        タスク設定コマンド実行
        param message:受け取ったメッセージの文字列
        return:botが応答するメッセージ
        """

        # メッセージレベル出力可能チェック
        if not self.can_output_level():
            return ""

        # コマンドチェック
        errmsg = self.get_errmsg_set_arg(message)

        # エラーがある場合はエラーメッセージを出力
        if errmsg:
            return errmsg

        args = message.split()

        name = args[1]
        person = ""
        progress = ""

        if len(args) > 2:
            opt_maps = common_utill.split_options(args[2:])
            person = (opt_maps[TaskMessenger.__OPTION_PERSON])[0] if TaskMessenger.__OPTION_PERSON in opt_maps else ""
            progress = (opt_maps[TaskMessenger.__OPTION_PROGRESS])[0] if TaskMessenger.__OPTION_PROGRESS in opt_maps else ""

        task = TaskInfo(name, person, progress)
        manager = TaskManager()

        if not manager.exist_task(name):
            manager.add_task(task)
        else:
            manager.upd_task(task)

        return "タスクを設定しました。  " + name + " 担当：" + person + "  進捗:" + progress + "%"

    def get_errmsg_set_arg(self, msg):
        """
        入力コマンドチェック処理
        param msg:受け取ったメッセージの文字列
        return:エラーありの場合はエラーメッセージ
               エラーなしの場合は空文字
        """

        args = msg.split()

        if len(args) < 2:
             return "タスク名が未入力です。\n" + self.__SETTASK_USAGE

        if len(args[1]) > 20:
            return "タスク名は２０字以下で指定してください。\n" + self.__SETLEVEL_USAGE

        # オプションが指定されていない場合は非エラー
        if len(args) == 2:
            return ""

        try:
            opt_maps = common_utill.split_options(args[2:])
        except InvalidCommandException:
            return "コマンドが不正です。\n" + self.__SETTASK_USAGE

        for k in opt_maps.keys():
            if(k != TaskMessenger.__OPTION_PERSON and k != TaskMessenger.__OPTION_PROGRESS):
                print("不正オプション：" + k)
                return "コマンドが不正です。\n" + self.__SETTASK_USAGE

        return ""

    def get_errmsg_list_arg(self, msg):
        """
        入力コマンドチェック処理
        param msg:受け取ったメッセージの文字列
        return:エラーありの場合はエラーメッセージ
               エラーなしの場合は空文字
        """

        args = msg.split()

        # オプションが指定されていない場合は非エラー
        if len(args) == 1:
            return ""

        try:
            opt_maps = common_utill.split_options(args[1:])
        except InvalidCommandException:
            return "コマンドが不正です。\n" + self.__SETTASK_USAGE

        for k in opt_maps.keys():
            if(k != TaskMessenger.__OPTION_PERSON and k != TaskMessenger.__OPTION_PROGRESS):
                print("不正オプション：" + k)
                return "コマンドが不正です。\n" + self.__SETTASK_USAGE

        return ""
