# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from plugins.outputlevel.OutputLevelMessenger import OutputLevelMessenger

@respond_to(r'^setlevel\s+\S.*')
def mention_func(message):
    output_level_msg = OutputLevelMessenger()
    rep = output_level_msg.exec_set(message.body['text'])
    message.reply(rep)
