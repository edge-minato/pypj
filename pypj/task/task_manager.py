from enum import Enum
from typing import List

from ..const import Emoji
from ..file_path import PypjFilePath
from ..setting import PypjSetting
from .githubactions import GithubActions
from .makefile import Makefile
from .precommit import PreCommit
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
    PRE_COMMIT = PreCommit


class TaskManager:
    def __init__(self, setting: PypjSetting, file_path: PypjFilePath) -> None:
        self.setting = setting
        self.file_path = file_path
        self.task_list: List[Task] = []
        self.add(Tasks.README)
        self.add(Tasks.PYPROJECT)
        self.reflect_setting_to_tasks()

    def add(self, task_name: Tasks) -> None:
        task = task_name.value(self.setting, self.file_path)
        for t in self.task_list:
            if task.name == t:
                return
        self.task_list.append(task)  # register

    def reflect_setting_to_tasks(self) -> None:
        s = self.setting
        self.add(Tasks.GITHUB_ACTIONS) if s.guthub_actions else None
        self.add(Tasks.VSCODE) if s.vscode else None
        self.add(Tasks.MAKEFILE) if s.makefile else None
        self.add(Tasks.PRE_COMMIT) if self.setting.precommit else None

    def execute(self) -> None:
        for task in self.task_list:
            task.execute()
        self.complete_message()

    def complete_message(self) -> None:
        print()
        print(f"Complete! {Emoji.LETS_GO} ")
        if self.setting.precommit:
            print('Note: Hit "make update" to update pre-commit hooks.')
        print(f"Let's make the world better! {Emoji.OK}{Emoji.PERFECT}{Emoji.PYTHON}{Emoji.WORLD}")
