# -*- coding: utf-8 -*-

from slacker import Slacker
import slackbot_settings
import urllib
import json
from datetime import datetime, timedelta, tzinfo
from time import sleep

if __name__ == '__main__':
        slack = Slacker(slackbot_settings.API_TOKEN)

class JST(tzinfo):
    """タイムゾーン定義クラス（日本標準時）"""
    def utcoffset(self,dt):
        return timedelta(hours=9)

    def dst(self,dt):
        return timedelta(0)

    def tzname(self,dt):
        return 'JST'

class WeatherForecast:
    """天気情報取得クラス"""
    text = None

    def __init__(self):
        """Wheather Hacksから天気の情報取得、'130010'は東京のID"""
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
        city_id = '130010'

        html = urllib.request.urlopen(url+city_id)
        jsonfile = json.loads(html.read().decode('utf-8'))
        self.text = jsonfile['description']['text']



while True:
    """無限ループさせて今の時間を所得させ、７時になったら実行"""
    now = datetime.now(tz=JST())
    if now.hour != 22 or now.minute != 54 or now.second != 00:
        continue

    """以下の文章を出力"""
    slack.chat.post_message('#general','おはようございます。',as_user=True)
    slack.chat.post_message('#general','今日の天気をお送りします。',as_user=True)
    weather = WeatherForecast() #インスタンス生成
    slack.chat.post_message('#general',weather.text,as_user=True)
    sleep(1)



# python3 WeatherForecast.py で実行


