# -*- coding: utf-8 -*-

class TaskManager(object):
    """タスク管理クラス"""

    __instance = None
    """自クラスのインスタンス"""

    def __new__(clsObj, *args, **kwargs):
        """シングルトンとする"""
        if not hasattr(clsObj, "__instance__"):
            clsObj.__instance__ = super(TaskManager, clsObj).__new__(clsObj, *args, **kwargs)
        return clsObj.__instance__

    def __init__(self, *args, **kwargs):
        """コンストラクタ"""
        # タスクのリスト
        self.task_list = []

    def add_task(self, task):
        """タスクリストにタスクを追加します"""
        if self.exist_task(task.task_name):
            raise Exception("登録済みのタスクです")

        self.task_list.append(task)

    def del_task(self, task):
        """タスクリストからタスクを削除します"""

        if not self.exist_task(task.task_name):
            raise Exception("指定タスクは存在しません")

        self.task_list.remove(target)

    def upd_task(self, task):
        """タスクリスト内のタスクを更新します"""

        target = self.get_task_by_name(task.task_name)

        if not target:
            raise Exception("指定タスクは存在しません")

        target = task

    def get_task_by_name(self, name):
        """タスクリスト内から一致するタスク名のタスクを取得します"""

        target = list(filter(lambda t:t.task_name == name, self.task_list))

        if target:
            return target[0]

        return None

    def get_task(self, name, person, progress):
        """タスクリスト内から一致するタスク名のタスクを取得します"""

        target = list(filter(lambda t:
        (t.task_name == name or not name)
        and (t.task_person == person or not person)
        and (t.task_progress == progress or (not person and t.task_progress != 100) )
        , self.task_list))

        if target:
            return target[0]

        return None
    def exist_task(self, name):
        """タスクがタスクリストに存在するか取得します"""

        target = list(filter(lambda t:t.task_name == name, self.task_list))
        if target:
            return True
        return False
