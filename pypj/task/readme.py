from pypj.const import INDENT, Emoji
from pypj.file_path import PypjFilePath
from pypj.resource import get_my_resource
from pypj.setting import PypjSetting
from pypj.task.task import Task


class Readme(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Readme"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Create README.md")
        # write README.md
        with self.path.readme_md.open(mode="w") as f:
            f.write(get_my_resource("README.md"))
        print(f"{INDENT}Create : README.md {Emoji.OK}")
