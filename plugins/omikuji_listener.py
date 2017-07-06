# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import random

from plugins.common.output_level_manager import OutputLevelManager

@respond_to('おみくじ')
def listen_set(message):
    """おみくじ"""
    if not can_output_msg:
        return

    run = random.randint(0, 100)
    if run == 0:
        message.reply("あなたの運勢は最凶です。今日死にまーす。")
    elif run >= 1 and run <=50:
        message.reply("末吉です。無難な１日となるでしょう。")
    elif run >= 51 and run <=90:
        message.reply("吉です。ラッキーカラーはセルリアンブルー！")
    elif run >= 91 and run <=100:
        message.reply("大吉です。おめでとうございます。")

def can_output_msg():
    """メッセージ出力可能かチェック"""
    if 8 <= OutputLevelManager.get_output_level():
        return True

    return False
