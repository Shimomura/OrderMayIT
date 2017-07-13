# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from plugins.outputlevel.output_level_messenger import OutputLevelMessenger
from plugins.task.task_messenger import TaskMessenger
from plugins.memo.memo_messenger import MemoMessenger
from plugins.common.mode_manager import ModeManager
from plugins.common.mode_manager import ProcessModeEnum
from plugins import exec_mode

@default_reply()
def default_msg(message):

    if ModeManager.now_mode is ProcessModeEnum.Normal:
        message.reply("なにか言った？")
    else:
        msg = exec_mode.exec_mode(message.body['text'])
        if msg:
            message.reply(msg)

@respond_to(r'^setlevel\s+\S.*')
def listen_set(message):
    """メッセージレベル設定コマンド"""
    output_level_msg = OutputLevelMessenger()
    rep = output_level_msg.exec_set(message.body['text'])
    print(rep)
    if rep:
        print(rep)
        message.reply(rep)

@respond_to('displevel')
def listen_set(message):
    """メッセージレベル表示コマンド"""
    output_level_msg = OutputLevelMessenger()
    rep = output_level_msg.exec_disp(message.body['text'])
    if rep:
        message.reply(rep)

@respond_to(r'^settask\s+\S.*')
def listen_set(message):
    """タスク設定コマンド"""
    messenger = TaskMessenger()
    rep = messenger.exec_set(message.body['text'])
    if rep:
        message.reply(rep)

@respond_to(r'^listtask')
def listen_set(message):
    """タスク表示コマンド"""
    messenger = TaskMessenger()
    rep = messenger.exec_list(message.body['text'])
    if rep:
        message.reply(rep)

@respond_to(r'^メモして')
def listen_set(message):
    """メモ保存モードに切り替え"""
    #TODO 改行が入った場合の対応
    ModeManager.now_mode = ProcessModeEnum.MemoSave
    message.reply("はーい。メモしまーす。")

@respond_to(r'^メモ見せて')
def listen_set(message):
    """メモ表示モードに切り替え"""
    ModeManager.now_mode = ProcessModeEnum.MemoDisp
    msg = "どのメモを見ますか？\n"
    messenger = MemoMessenger()
    msg += messenger.exec_list()
    message.reply(msg)

@respond_to(r'^メモ削除')
def listen_set(message):
    """メモ削除モードに切り替え"""
    ModeManager.now_mode = ProcessModeEnum.MemoDel
    msg = "どのメモを削除しますか？\n"
    messenger = MemoMessenger()
    msg += messenger.exec_list()
    message.reply(msg)
