from pypj.const import INDENT, Emoji
from pypj.file_path import PypjFilePath
from pypj.resource import get_my_resource
from pypj.setting import PypjSetting
from pypj.task.task import Task
from pypj.utils import setValue


class Makefile(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Makefile"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Create makefile")
        makefile_path = "Makefile_precommit" if self.setting.precommit else "Makefile"
        with self.path.makefile.open(mode="w") as f:
            f.write(setValue(self.setting.replace_words, get_my_resource(makefile_path)))
        print(f"{INDENT}Create : Makefile {Emoji.OK}")
