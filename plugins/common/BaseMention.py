# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import OutputLevelManager

class BaseMention(Object):
    """メンション基底クラス"""

    __metaclass__ = ABCMeta

    __mention_output_level = 11
    """
    メッセージの出力レベル
    デフォルトは１１：一切出力なし
    """

    @abstractmethod
    def set_mention_level(self, level):
        """
        メッセージの出力レベル設定
        param level:設定するメッセージ出力レベル
        """
        raise NotImplementedError()

    def get_mention_level(self):
        """
        メッセージの出力レベル取得
        return:メッセージ出力レベル
        """
        return __mention_output_level

    def check_output_level():
        """
        メッセージが出力可能か出力レベル設定をチェックする
        return: True:出力可能 False:出力不可
        """
        if __mention_output_level <= OutputLevelManager.get_output_level():
            return True

        return False
