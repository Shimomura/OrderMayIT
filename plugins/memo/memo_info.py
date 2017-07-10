# -*- coding: utf-8 -*-

class MemoInfo:
    """メモ情報クラス"""

    def __init__(self, num, content, date):
        """
        コンストラクタ
        param num:メモNo
        param content:メモ内容
        param date:作成日付
        """
        self.memo_No = num
        self.memo_contents = content
        self.memo_date = date
