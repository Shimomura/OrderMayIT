# -*- coding: utf-8 -*-

from slacker import Slacker
import slackbot_settings
import urllib
import json
from datetime import datetime
from time import sleep

if __name__ == '__main__':
        slack = Slacker(slackbot_settings.API_TOKEN)

while True:
    """無限ループさせて今の時間を所得させ、７時になったら実行"""

    if datetime.now().hour == 7 and datetime.now().minute == 00 and datetime.now().second == 00:
        """Wheather Hacksから天気の情報取得、'130010'は東京のID"""
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
        city_id = '130010'

        html = urllib.request.urlopen(url+city_id)
        jsonfile = json.loads(html.read().decode('utf-8'))
        text = jsonfile['description']['text']

        slack.chat.post_message('#general','おはようございます。',as_user=True)
        slack.chat.post_message('#general','今日の天気をお送りします。',as_user=True)
        slack.chat.post_message('#general',text,as_user=True)
        sleep(1)


# python3 WeatherForecast.py で実行

