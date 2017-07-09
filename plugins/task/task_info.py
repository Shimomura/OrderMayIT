# -*- coding: utf-8 -*-

class TaskInfo:
    """タスク情報クラス"""

    def __init__(self, name, person, progress):
        """
        コンストラクタ
        param name:タスク名
        param person:担当者
        param progress:進捗
        """
        self.task_name = name
        self.task_person = person
        self.task_progress = progress

    
