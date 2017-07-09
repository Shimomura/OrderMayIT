# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from plugins.outputlevel.output_level_messenger import OutputLevelMessenger
from plugins.task.task_messenger import TaskMessenger

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
