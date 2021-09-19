from ..const import INDENT, Emoji
from ..file_path import PypjFilePath
from ..resource import get_my_resource
from ..setting import PypjSetting
from .task import Task


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
