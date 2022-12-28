from pypj.const import INDENT, Emoji
from pypj.file_path import PypjFilePath
from pypj.resource import get_my_resource
from pypj.setting import PypjSetting
from pypj.task.task import Task
from pypj.utils import setValue


class Vscode(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Vscode"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Configure vscode settings")
        # mkdir .vscode
        self.path.vscode_dir.mkdir()
        # write settings
        with self.path.vscode_settings_json.open(mode="w") as f:
            f.write(setValue(self.setting.replace_words, get_my_resource("settings.json")))
        print(f"{INDENT}Create : .vscode/settings.json {Emoji.OK}")
