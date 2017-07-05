# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from plugins.common.OutputLevelManager import OutputLevelManager

@respond_to('こんにちは')
def listen_set(message):
    """こんにちは"""
    if not can_output_msg:
        return
    message.reply("やぁ")

@respond_to('こんばんは')
def listen_set(message):
    """こんばんは"""
    if not can_output_msg:
        return
    message.reply("今日は月が綺麗ですね")

@respond_to('おはよう')
def listen_set(message):
    """おはよう"""
    if not can_output_msg:
        return
    message.reply("お、今日は早いね")

def can_output_msg():
    """メッセージ出力可能かチェック"""
    if 8 <= OutputLevelManager.get_output_level():
        return True

    return False
