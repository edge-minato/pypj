#!/usr/bin/env python3
import sys
from pathlib import Path
from traceback import format_exc

from pypj.cui import ask_no_empty, ask_yN, confirm_proceed

from .args import args
from .const import ASCII_ART, GITHUB_URL
from .environment import Environment
from .exception import PypjError
from .file_path import PypjFilePath
from .setting import PackageName, PypjSetting
from .task import Poetry, TaskManager


def ask_package_name() -> PackageName:
    r = ask_no_empty("Package name: ")
    return PackageName(r) if PackageName.is_valid(r) else ask_package_name()


def process() -> None:
    # preprocess
    env = Environment()
    print(ASCII_ART.format(python=env.python, poetry=env.poetry))
    # configure
    setting = PypjSetting(python_version=env.python, package_name=ask_package_name())
    if ask_yN("Do you want to customize settings?"):
        setting.customize()
    pypj_file_path = PypjFilePath(Path().cwd(), setting)
    # define tasks
    tm = TaskManager(setting, pypj_file_path)
    # execute
    confirm_proceed()
    Poetry(setting, pypj_file_path).execute()
    tm.execute()


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
    except Exception:
        print(format_exc())
        print()
        print("If you are behind a proxy, try to set following environmental variables.")
        print("http_proxy, https_proxy, HTTP_PROXY, HTTPS_PROXY")
        print(f"Else, please report the issue to {GITHUB_URL}")
        sys.exit(1)
