from enum import Enum


class Eenum(Enum):
    def __str__(self) -> str:
        return str(self.value)


class Formatter(Eenum):
    BLACK = "black"


class Linter(Eenum):
    FLAKE8 = "flake8"
    PFLAKE8 = "pyproject-flake8"


class ImportSorter(Eenum):
    ISORT = "isort"


class TypeChecker(Eenum):
    MYPY = "mypy"


class TestFramework(Eenum):
    PYTEST = "pytest"
    TOX = "tox"


class Plugin(Eenum):
    FLAKE8_BUGBEAR = "flake8-bugbear"
    PYTEST_COV = "pytest-cov"
    PYTEST_MOCK = "pytest-mock"
    TOX_GH_ACTIONS = "tox-gh-actions"
