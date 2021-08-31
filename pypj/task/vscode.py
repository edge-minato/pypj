from ..const import INDENT, Emoji
from ..file_path import PypjFilePath
from ..resource import get_my_resource
from ..setting import PypjSetting
from .task import Task


class Vscode(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Vscode"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Configure vscode settings")
        self.done_check()
        # get settings
        settings_jsonc = get_my_resource("settings.jsonc")
        settings_jsonc = settings_jsonc.replace("PACKAGE_NAME", self.setting.package_name)
        # mkdir .vscode
        self.path.vscode_dir.mkdir()
        # write settings
        with self.path.vscode_settings_json.open(mode="w") as f:
            f.write(settings_jsonc)
        print(f"{INDENT}Create : .vscode/settings.json {Emoji.OK}")
        self.done()
