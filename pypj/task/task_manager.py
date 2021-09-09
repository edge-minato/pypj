from enum import Enum
from typing import List

from ..const import Emoji
from ..file_path import PypjFilePath
from ..setting import PypjSetting
from .githubactions import GithubActions
from .makefile import Makefile
from .pyproject import Pyproject
from .readme import Readme
from .task import Task
from .vscode import Vscode


class Tasks(Enum):
    GITHUB_ACTIONS = GithubActions
    MAKEFILE = Makefile
    PYPROJECT = Pyproject
    README = Readme
    VSCODE = Vscode


class TaskManager:
    def __init__(self, setting: PypjSetting, file_path: PypjFilePath) -> None:
        self.setting = setting
        self.file_path = file_path
        self.task_list: List[Task] = []

    def add(self, task_name: Tasks) -> None:
        task = task_name.value(self.setting, self.file_path)
        for t in self.task_list:
            if task.name == t:
                return
        self.task_list.append(task)  # register

    def execute(self) -> None:
        for task in self.task_list:
            task.execute()
        self.complete_message()

    def complete_message(self) -> None:
        print()
        print(f"Complete! {Emoji.LETS_GO} ")
        print(f"Let's make the world better! {Emoji.OK}{Emoji.PERFECT}{Emoji.PYTHON}{Emoji.WORLD}")
