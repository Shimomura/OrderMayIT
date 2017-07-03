# -*- coding: utf-8 -*-

from plugins.common.OutputLevelManager import OutputLevelManager

class BaseMessenger(object):
    """メッセンジャー基底クラス"""

    def __init__(self, level):
        """コンストラクタ"""

        # メッセージの出力レベルを保持するインスタンス変数
        self.message_output_level = level

    def can_output_level(self):
        """
        メッセージが出力可能か出力レベル設定をチェックする
        return: True:出力可能 False:出力不可
        """
        if self.message_output_level <= OutputLevelManager.get_output_level():
            return True

        return False
