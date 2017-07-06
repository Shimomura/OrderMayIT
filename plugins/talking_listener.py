# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random

from plugins.common.output_level_manager import OutputLevelManager

@respond_to('いくつ')
def listen_set(message):
    """DIO様"""
    if not can_output_msg:
        return
    message.reply("お前は今まで食べたパンの数を覚えているか？")

@respond_to('何人')
def listen_set(message):
    """DIO様"""
    if not can_output_msg:
        return
    message.reply("お前は今まで食べたパンの数を覚えているか？")

@respond_to('調子はどう')
def listen_set(message):
    """調子"""
    if not can_output_msg:
        return
    run = random.randint(0, 2)
    if run == 0:
        message.reply("ぼちぼちでんな")
    elif run == 1:
        message.reply("最低です")
    if run == 2:
        message.reply("最高に「ハイ！」ってやつだアアアアアアハハハハハハハハハハーッ")



def can_output_msg():
    """メッセージ出力可能かチェック"""
    if 8 <= OutputLevelManager.get_output_level():
        return True

    return False
