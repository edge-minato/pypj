#!/usr/bin/env python3
import os
import pkgutil
import sys
from pathlib import Path

from .args import args
from .const import ASCII_ART, POETRY_INSTALL_GUIDE, Emoji
from .cui import ask_no_empty, ask_with_default_num, ask_Yn, ask_yN
from .environment import Environment, Platform, Version
from .exception import Emsg, PypjError
from .poetry import poetry_add, poetry_new
from .setting import BLACK_SETTING, FLAKE8_SETTING, ISORT_SETTING, MYPY_SETTING, PypjSetting


def configure_pyproject_toml(setting: PypjSetting, python_version: Version) -> None:
    file = Path("./pyproject.toml")
    with file.open(mode="a") as f:
        f.write(BLACK_SETTING.format(line_length=setting.max_line_length))
        f.write(FLAKE8_SETTING.format(line_length=setting.max_line_length))
        f.write(MYPY_SETTING.format(python_version=python_version.short))
        f.write(ISORT_SETTING.format(formatter=setting.formatter, line_length=setting.max_line_length))


def generate_vscode_setting_json() -> None:
    # resource
    resource = pkgutil.get_data("pypj", "settings.jsonc")
    if resource is None:
        raise PypjError(Emsg.RESOURCE_NOT_FOUND)
    vscode_setting = resource.decode("utf-8")
    # dir
    directory = Path(".vscode")
    if not directory.is_dir():
        print(f"  Create : .vscode directory {Emoji.OK}")
        directory.mkdir()
    # file
    ORIGINAL = "settings.json"
    ANOTHER = "settings.pypj.json"
    file_name = ANOTHER if directory.joinpath("settings.json").exists() else ORIGINAL
    output_file = directory.joinpath(file_name)
    with output_file.open(mode="w") as f:
        f.write(vscode_setting)
    print(f"  Create : .vscode/{file_name} {Emoji.OK}")


def process() -> None:
    # init
    env = Environment()
    print(ASCII_ART.format(python=env.python, poetry=env.poetry))
    # Check OS is unix
    if env.os is not Platform.UNIX:
        print("This operating system is not supported but you can try.")
        if not ask_yN("Do you want to proceed? (y/N): "):
            print("Canceld.")
            sys.exit(0)
    # Check poetry
    if env.poetry is None:
        print("Please install poetry first.")
        print(f"Reference: {POETRY_INSTALL_GUIDE}")
        sys.exit(0)
    # Main process
    package_name = ask_no_empty("Package name: ")
    setting = PypjSetting(package_name)
    custom = ask_yN("Do you want to use customized setting? (y/N): ")
    if custom:
        setting.max_line_length = ask_with_default_num("Max line length (119): ", 119)
        setting.src_flag = ask_yN("Do you want to use src folder? (y/N): ")
        setting.venv_in_pj = ask_Yn("Do you want to keep venv in project? (Y/n): ")
        confirmation = ask_yN("Are you sure? (y/N): ")
        if not confirmation:
            print("Canceled.")
            sys.exit(0)
    poetry_new(setting)
    os.chdir(setting.package_name)
    generate_vscode_setting_json()
    configure_pyproject_toml(setting, env.python)
    poetry_add(setting)
    print()
    print(f"Complete! {Emoji.LETS_GO} ")
    print(f"Let's make the world better! {Emoji.OK}{Emoji.PERFECT}{Emoji.PYTHON}{Emoji.WORLD}")


def main() -> None:
    try:
        args()
        process()
    except PypjError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print("Canceled.")
        sys.exit(1)
    except Exception as e:
        print("If you are behind a proxy, try to set following environmental variables.")
        print("http_proxy, https_proxy, HTTP_PROXY, HTTPS_PROXY")
        raise e
