#!/usr/bin/env python3
import sys
from pathlib import Path
from traceback import format_exc

from pypj.task.githubactions import GithubActions
from pypj.task.readme import Readme

from .args import args
from .const import ASCII_ART, complete_message
from .environment import Environment
from .exception import PypjError
from .file_path import PypjFilePath
from .setting import PypjSetting
from .task import Makefile, Poetry, Pyproject, Vscode


def process() -> None:
    # check env
    env = Environment()
    print(ASCII_ART.format(python=env.python, poetry=env.poetry))
    # preprocess
    setting = PypjSetting(env.python)
    setting.package_name_validate()
    setting.customize()
    pypj_file_path = PypjFilePath(Path().cwd(), setting)
    # execute tasks
    Poetry(setting, pypj_file_path).execute()
    Vscode(setting, pypj_file_path).execute()
    Pyproject(setting, pypj_file_path).execute()
    Makefile(setting, pypj_file_path).execute()
    GithubActions(setting, pypj_file_path).execute()
    Readme(setting, pypj_file_path).execute()
    # complete
    complete_message()


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
        print("If you are behind a proxy, try to set following environmental variables.")
        print("http_proxy, https_proxy, HTTP_PROXY, HTTPS_PROXY")
        sys.exit(1)
