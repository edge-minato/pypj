from ..const import INDENT, Emoji
from ..file_path import PypjFilePath
from ..resource import get_my_resource
from ..setting import PypjSetting
from .task import Task


class PreCommit(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Pre-commit"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Configure pre-commit ")
        self.done_check()
        precommit = get_my_resource(".pre-commit-config.yaml")
        with self.path.precommit.open(mode="w") as f:
            f.write(precommit)
        print(f"{INDENT}Create : .pre-commit-config.yaml {Emoji.OK}")
        self.done()
