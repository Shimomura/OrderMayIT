# -*- coding: utf-8 -*-

class TaskManager:
    """タスク管理クラス"""

    __instance = None
    """自クラスのインスタンス"""

    def __init__(self):
        """コンストラクタ"""
        # タスクのリスト
        self.task_list = []

    def __new__(cls):
        """シングルトンとする"""
        if cls.__instance is None:
            cls._instance = super().__new__(cls)

        return cls.__instance

    def add_task(self, task):
        """タスクリストにタスクを追加します"""

        if filter(lambda t:t.task_name == task.task_name, self.task_list)
            raise Exception("登録済みのタスクです")

        self.task_list.append(task)

    def del_task(self, task):
        """タスクリストからタスクを削除します"""

        target = filter(lambda t:t.task_name == task.task_name, self.task_list)

        if not target:
            raise Exception("指定タスクは存在しません")

        self.task_list.remove(target)

    def upd_task(self, task):
        """タスクリスト内のタスクを更新します"""

        target = filter(lambda t:t.task_name == task.task_name, self.task_list)

        if not target:
            raise Exception("指定タスクは存在しません")

        target = task

    def get_task(self, name):
        """タスクリスト内から一致するタスク名のタスクを取得します"""

        return filter(lambda t:t.task_name == name, self.task_list)
