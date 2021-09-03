from ..const import INDENT, Emoji
from ..file_path import PypjFilePath
from ..setting import BLACK_SETTING, FLAKE8_SETTING, ISORT_SETTING, MYPY_SETTING, PypjSetting
from .task import Task


class Pyproject(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Pyproject"
        super().__init__(name, setting, path)

    def execute(self) -> None:
        print("Task: Configure pyproject.toml settings")
        self.done_check()
        mll = self.setting.max_line_length
        pv = self.setting.python_version.short
        fmt = self.setting.formatter
        with self.path.pyproject.open(mode="a") as f:
            f.write(BLACK_SETTING.format(line_length=mll))
            f.write(FLAKE8_SETTING.format(line_length=mll))
            f.write(MYPY_SETTING.format(python_version=pv))
            f.write(ISORT_SETTING.format(formatter=fmt, line_length=mll))
        print(f"{INDENT}Write  : pyproject.toml {Emoji.OK}")
        self.done()
