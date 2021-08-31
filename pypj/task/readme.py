from ..const import INDENT, Emoji
from ..file_path import PypjFilePath
from ..resource import get_my_resource
from ..setting import PypjSetting
from .task import Task


class Readme(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Readme"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Create README.md")
        self.done_check()
        # delete README.rst
        self.path.readme_rst.unlink()
        # write README.md
        readme = get_my_resource("README.md")
        with self.path.readme_md.open(mode="w") as f:
            f.write(readme)
        print(f"{INDENT}Create : README.md {Emoji.OK}")
        self.done()
