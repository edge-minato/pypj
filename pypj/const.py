from enum import Enum
from pathlib import Path

from single_source import get_version

VERSION = get_version(__package__, Path(__file__).parent.parent)

AUTHOR = "edge-minato"
GITHUB_URL = "https://github.com/edge-minato/pypj"
POETRY_INSTALL_GUIDE = "https://python-poetry.org/docs/#installation"
PACKAGE = "pypj"
ASCII_ART = """
┌─┐┬ ┬┌─┐┬
├─┘└┬┘├─┘│    python : {python}
┴   ┴ ┴ └┘    poetry : {poetry}
"""
HELP = """
┌─┐┬ ┬┌─┐┬    version: {version}
├─┘└┬┘├─┘│    author : {author}
┴   ┴ ┴ └┘    github : {github}
""".format(
    version=VERSION, author=AUTHOR, github=GITHUB_URL
)


class Emoji(Enum):
    OK = "✨"
    NG = "🔥"
    WAIT = "⏳"
    PERFECT = "😋"
    PYTHON = "🐍"
    LETS_GO = "🚀"
    WORLD = "🌎"

    def __str__(self) -> str:
        return self.value


INDENT = " " * 6


def complete_message() -> None:
    print()
    print(f"Complete! {Emoji.LETS_GO} ")
    print(f"Let's make the world better! {Emoji.OK}{Emoji.PERFECT}{Emoji.PYTHON}{Emoji.WORLD}")
