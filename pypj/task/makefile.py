from pypj.const import INDENT, Emoji
from pypj.file_path import PypjFilePath
from pypj.resource import get_my_resource
from pypj.setting import PypjSetting
from pypj.task.task import Task


class Makefile(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Makefile"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Create makefile")
        self.done_check()
        makefile_path = "Makefile_precommit" if self.setting.precommit else "Makefile"
        makefile = get_my_resource(makefile_path).replace("PACKAGE_SRC_DIR", self.setting.src_dir)
        with self.path.makefile.open(mode="w") as f:
            f.write(makefile)
        print(f"{INDENT}Create : Makefile {Emoji.OK}")
        self.done()
