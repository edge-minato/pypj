from enum import Enum


class Emsg(Enum):
    OS_NOT_SUPPORTED = "Pypj only supports unix system."
    PIP_NOT_FOUND = "pip is not installed."
    FAILED_GET_POETRY_VER = "Failed to get poetry version."
    FAILED_POETRY_NEW = "Failed to 'poetry new'."
    FAILED_POETRY_CONFIG = "Failed to configure poetry."
    FAILED_POETRY_ADD = "Failed to add package via poetry."
    RESOURCE_NOT_FOUND = "settings.jsonc does not found. Please report this issue."

    def __str__(self) -> str:
        return self.name


class PypjError(Exception):
    def __init__(self, message: Emsg):
        self.message = message.value
        super().__init__(self.message)
