from os import chdir
from subprocess import PIPE, CompletedProcess, run

from pypj.const import INDENT, Emoji
from pypj.file_path import PypjFilePath
from pypj.resource import get_my_resource
from pypj.setting import PypjSetting
from pypj.task.task import Task, TaskError


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
        self.__new()
        self.__configure_poetry()
        chdir(self.path.package_dir)
        self.__add_dev_dependency()
        self.__add_dependency()
        self.__overwrite_files()
        print(f"{INDENT}Create : {self.setting.package_name} {Emoji.OK}")

    def __command(self, cmd: str) -> CompletedProcess:
        print(f"{INDENT}Command: {cmd} {Emoji.WAIT}", end="", flush=True)
        r = run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        status = Emoji.OK if r.returncode == 0 else Emoji.NG
        print(f"\r{INDENT}Command: {cmd} {status}", flush=True)
        return r

    def __replace_python_version(self) -> None:
        current = f'python = "^{self.setting.python_version.short}"'
        new = f'python = "^{self.setting.python_version.version}"'

        with self.path.pyproject.open("r") as f:
            content = str(f.read())
        if current not in content:
            print(content)
            raise TaskError(f"Failed to find '{current}' in pyproject.toml")
        with self.path.pyproject.open("w") as f:
            f.write(content.replace(current, new))

    def __new(self) -> None:
        # poetry new
        r = self.__command(self.poetry_new_cmd)
        if r.returncode != 0:
            raise TaskError(f"Failed to '{self.poetry_new_cmd}'")
        self.__replace_python_version()
        print(f"{INDENT}Poetry new done {Emoji.LETS_GO}")

    def __configure_poetry(self) -> None:
        r = self.__command(self.venv_in_pj_cmd)
        if r.returncode != 0:
            raise TaskError(f"Failed to '{self.venv_in_pj_cmd}'")

    def __add_dependency(self) -> None:
        ADD_CMD = "poetry add {}"
        packages = ["single-source"]
        command_list = [ADD_CMD.format(package) for package in packages]
        for cmd in command_list:
            r = self.__command(cmd)
            if r.returncode != 0:
                raise TaskError(f"Failed to add dependency: {cmd}")

    def __add_dev_dependency(self) -> None:
        ADD_CMD = "poetry add --group dev {}"
        dev_packages = [
            self.setting.formatter,
            self.setting.linter,
            self.setting.type_checker,
            self.setting.import_sorter,
            self.setting.unittest_framework,
            self.setting.test_framework,
        ]
        command_list = [ADD_CMD.format(package) for package in dev_packages]
        for plugin in self.setting.plugin:
            command_list.append(ADD_CMD.format(plugin))
        if self.setting.precommit:
            command_list.append(ADD_CMD.format("pre-commit"))
        for cmd in command_list:
            r = self.__command(cmd)
            if r.returncode != 0:
                raise TaskError(f"Failed to add dev dependency: {cmd}")

    def __overwrite_files(self) -> None:
        # __init__.py
        init_path = "package/init.py"
        init = get_my_resource(init_path)
        with self.path.package_init.open(mode="w") as f:
            f.write(init)
        # test_{package}.py
        test_path = "package/test_package.py"
        test = get_my_resource(test_path).replace("PACKAGE_NAME", self.setting.package_name)
        with self.path.package_test.open(mode="w") as f:
            f.write(test)
