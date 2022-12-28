from pypj.const import INDENT, Emoji
from pypj.file_path import PypjFilePath
from pypj.resource import get_my_resource
from pypj.setting import PypjSetting
from pypj.task.task import Task
from pypj.utils import setValue


class GithubActions(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "GithubActions"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Create github actions")
        # prepare directory
        self.path.github_dir.mkdir()
        self.path.github_workflow_dir.mkdir()
        # write workflows *.yml
        for file in (self.path.wf_unittest, self.path.wf_publish, self.path.dependabot):
            with file.open(mode="w") as f:
                f.write(setValue(self.setting.replace_words, get_my_resource(file.name)))
            print(f"{INDENT}Create : {file.name} {Emoji.OK}")
