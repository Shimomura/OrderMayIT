# -*- coding: utf-8 -*-

class OutputLevelManager:
    """出力レベル管理クラス"""

    __output_level = 10
    """出力レベル"""

    @staticmethod
    def set_output_level(level):
        """
        出力レベルを設定する
        param level:設定する出力レベル
        """
        if not isinstance(level, int):
            raise Exception("出力レベルに整数以外を設定しようとしました level:" + str(level))
        if level > 10 or level < 0:
            raise Exception("出力レベルに設定できるのは１以上１０以下の整数です level:" +str(level))

        OutputLevelManager.__output_level = level

    @staticmethod
    def get_output_level():
        """
        出力レベルを取得する
        return:出力レベル
        """
        return OutputLevelManager.__output_level
