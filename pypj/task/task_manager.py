from enum import Enum
from typing import List

from ..const import Emoji
from ..cui import ask_Yn
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
    def __init__(self, setting: PypjSetting, file_path: PypjFilePath, customize: bool) -> None:
        self.setting = setting
        self.file_path = file_path
        self.task_list: List[Task] = []
        self.add(Tasks.README)
        self.add(Tasks.PYPROJECT)

        if customize:
            self.customize()
        else:
            self.default()

    def add(self, task_name: Tasks) -> None:
        task = task_name.value(self.setting, self.file_path)
        for t in self.task_list:
            if task.name == t:
                return
        self.task_list.append(task)  # register

    def default(self) -> None:
        self.add(Tasks.GITHUB_ACTIONS)
        self.add(Tasks.VSCODE)
        self.add(Tasks.MAKEFILE)

    def customize(self) -> None:
        if ask_Yn("Do you want configured github workflows? (Y/n): "):
            self.add(Tasks.GITHUB_ACTIONS)
        if ask_Yn("Do you want configured vscode settings? (Y/n): "):
            self.add(Tasks.VSCODE)
        if ask_Yn("Do you want command alias as Makefile? (Y/n): "):
            self.add(Tasks.MAKEFILE)

    def execute(self) -> None:
        for task in self.task_list:
            task.execute()
        self.complete_message()

    def complete_message(self) -> None:
        print()
        print(f"Complete! {Emoji.LETS_GO} ")
        print(f"Let's make the world better! {Emoji.OK}{Emoji.PERFECT}{Emoji.PYTHON}{Emoji.WORLD}")
