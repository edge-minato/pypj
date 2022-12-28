from pypj.const import INDENT, Emoji
from pypj.file_path import PypjFilePath
from pypj.resource import get_my_resource
from pypj.setting import PypjSetting
from pypj.task.task import Task


class PreCommit(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Pre-commit"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Configure pre-commit ")
        precommit = get_my_resource(".pre-commit-config.yaml")
        with self.path.precommit.open(mode="w") as f:
            f.write(precommit)
        print(f"{INDENT}Create : .pre-commit-config.yaml {Emoji.OK}")
