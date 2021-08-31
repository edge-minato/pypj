from abc import ABC, abstractmethod
from enum import Enum, auto

from ..file_path import PypjFilePath
from ..setting import PypjSetting


class TaskError(Exception):
    pass


class TaskStatus(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()


class Task(ABC):
    def __init__(self, name: str, setting: PypjSetting, path: PypjFilePath) -> None:
        self.name: str = name
        self.status: TaskStatus = TaskStatus.TODO
        self.setting = setting
        self.path = path

    def done(self) -> None:
        self.status = TaskStatus.DONE

    def is_done(self) -> bool:
        return True if self.status is TaskStatus.DONE else False

    def done_check(self) -> None:
        if self.is_done():
            raise TaskError("Task is already done.")

    @abstractmethod
    def execute(self) -> None:
        pass
