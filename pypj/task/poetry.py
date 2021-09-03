from os import chdir
from subprocess import PIPE, CompletedProcess, run

from ..const import INDENT, Emoji
from ..file_path import PypjFilePath
from ..resource import get_my_resource
from ..setting import PypjSetting
from .task import Task, TaskError


class Poetry(Task):
    def __init__(self, setting: PypjSetting, path: PypjFilePath) -> None:
        name = "Poetry"
        super().__init__(name, setting, path)
        self.setting = setting
        self.poetry_new_cmd = f"poetry new {setting.package_name}"
        if setting.use_src:
            self.poetry_new_cmd += " --src"
        self.venv_in_pj_cmd = f"poetry config virtualenvs.in-project {str(setting.venv_in_pj).lower()}"

    def execute(self) -> None:
        print(f"Task: Initialize package: {self.setting.package_name}")
        self.done_check()
        self.__new()
        self.__configure_poetry()
        chdir(self.path.package_dir)
        self.__add_dev_dependency()
        self.__overwrite_init()
        print(f"{INDENT}Create : {self.setting.package_name} {Emoji.OK}")
        self.done()

    def __command(self, cmd: str) -> CompletedProcess:
        print(f"{INDENT}Command: {cmd} {Emoji.WAIT}", end="", flush=True)
        r = run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        status = Emoji.OK if r.returncode == 0 else Emoji.NG
        print(f"\r{INDENT}Command: {cmd} {status}", flush=True)
        return r

    def __new(self) -> None:
        # poetry new
        r = self.__command(self.poetry_new_cmd)
        if r.returncode != 0:
            raise TaskError(f"Failed to '{self.poetry_new_cmd}'")
        print(f"{INDENT}Poetry new done {Emoji.LETS_GO}")

    def __configure_poetry(self) -> None:
        r = self.__command(self.venv_in_pj_cmd)
        if r.returncode != 0:
            raise TaskError(f"Failed to '{self.venv_in_pj_cmd}'")

    def __add_dev_dependency(self) -> None:
        ADD_CMD = "poetry add -D {}"
        dev_packages = [
            self.setting.formatter,
            self.setting.linter,
            self.setting.type_linter,
            self.setting.import_formatter,
            self.setting.test_fw,
            self.setting.tox,
        ]
        command_list = [ADD_CMD.format(package) for package in dev_packages]
        for plugin in self.setting.plugin:
            command_list.append(ADD_CMD.format(plugin))
        for cmd in command_list:
            r = self.__command(cmd)
            if r.returncode != 0:
                raise TaskError(f"Failed to add dev dependency: {cmd}")

    def __overwrite_init(self) -> None:
        init = get_my_resource("init.py")
        with self.path.package_init.open(mode="w") as f:
            f.write(init)
        print("{INDENT}Configure: __init__.py  {Emoji.OK}")
