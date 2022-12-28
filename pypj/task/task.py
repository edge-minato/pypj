from abc import ABC, abstractmethod
from typing import Optional

from pypj.file_path import PypjFilePath
from pypj.setting import PypjSetting


class TaskError(Exception):
    def __init__(self, *args: object, e: Optional[Exception] = None) -> None:
        self.e = e
        super().__init__(**args)


class Task(ABC):
    def __init__(self, name: str, setting: PypjSetting, path: PypjFilePath) -> None:
        self.name: str = name
        self.setting = setting
        self.path = path

    @abstractmethod
    def execute(self) -> None:
        pass
