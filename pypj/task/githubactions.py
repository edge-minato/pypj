from ..const import INDENT, Emoji
from ..file_path import PypjFilePath
from ..resource import get_my_resource
from ..setting import PypjSetting
from .task import Task


class GithubActions(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "GithubActions"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Create github actions")
        self.done_check()
        # prepare directory
        self.path.github_dir.mkdir()
        self.path.github_workflow_dir.mkdir()
        # write workflows *.yml
        unittest = get_my_resource("unittest.yml")
        unittest = unittest.replace("PYTHON_VERSION", self.setting.python_version.short)
        publish = get_my_resource("publish.yml")
        publish = publish.replace("PYTHON_VERSION", self.setting.python_version.short)
        dependabot = get_my_resource("dependabot.yml")
        with self.path.wf_unittest.open(mode="w") as f:
            f.write(unittest)
        print(f"{INDENT}Create : unittest.yml {Emoji.OK}")
        with self.path.wf_publish.open(mode="w") as f:
            f.write(publish)
        print(f"{INDENT}Create : publish.yml {Emoji.OK}")
        with self.path.dependabot.open(mode="w") as f:
            f.write(dependabot)
        print(f"{INDENT}Create : dependabot.yml {Emoji.OK}")
        self.done()
