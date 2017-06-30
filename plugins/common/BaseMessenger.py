# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from plugins.common.OutputLevelManager import OutputLevelManager

class BaseMessenger(object):
    """メッセージ基底クラス"""

    __metaclass__ = ABCMeta

    __message_output_level = 11
    """
    メッセージの出力レベル
    デフォルトは１１：一切出力なし
    """

    @abstractmethod
    def set_message_level(self, level):
        """
        メッセージの出力レベル設定
        param level:設定するメッセージ出力レベル
        """
        raise NotImplementedError()

    def set_message_output_level(self, level):
        """
        private変数 message_output_levelのsetter
        param level:設定する値
        """
        __message_output_level = level

    def get_message_level(self):
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
