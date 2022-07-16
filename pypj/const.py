from enum import Enum

from pypj import VERSION

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
