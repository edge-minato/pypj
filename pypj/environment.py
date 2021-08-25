"""
This file provides environment information and prerequisite checker.
"""
import platform
import shutil
from dataclasses import dataclass
from enum import Enum, auto
from subprocess import PIPE, run
from typing import Optional

from .exception import Emsg, PypjError


@dataclass
class Version(object):
    version: str
    separator: str = "."
    major: str = ""
    minor: str = ""
    patch: str = ""
    short: str = ""

    def __post_init__(self) -> None:
        v = self.version.split(self.separator)
        if len(v) == 3:
            self.major, self.minor, self.patch = v
        elif len(v) == 2:
            self.major, self.minor = v
        else:
            raise ValueError("The version does not contain minor version.")
        self.short = f"{self.major}{self.separator}{self.minor}"

    def __str__(self) -> str:
        return self.version


class Platform(Enum):
    WINDOWS = auto()
    UNIX = auto()
    OTHERS = auto()

    def __str__(self) -> str:
        return self.name


class Environment(object):
    def __init__(self) -> None:
        self.os: Platform = self.get_os()
        self.python: Version = self.get_python()
        self.poetry: Optional[Version] = self.get_poetry()

    def show(self) -> None:
        print(f"python : {self.python}")
        print(f"poetry : {self.poetry}")
        print()

    def get_os(self) -> Platform:
        pf = platform.system()
        if pf == "Windows":
            return Platform.WINDOWS
        elif pf in ["Darwin", "Linux"]:
            return Platform.UNIX
        else:
            return Platform.OTHERS

    def get_python(self) -> Version:
        return Version(platform.python_version())

    def get_poetry(self) -> Optional[Version]:
        POETRY = "poetry"
        POETRY_VER = "poetry --version"
        poetry_path = shutil.which(POETRY)
        if poetry_path is None:
            return None
        r = run(POETRY_VER, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        if r.returncode != 0:
            raise PypjError(Emsg.FAILED_GET_POETRY_VER)
        return Version(r.stdout.split()[2])  # "Poetry version 1.1.7"
