from enum import Enum


class Message(object):
    pass


class Emsg(Enum):
    OS_NOT_SUPPORTED = "Pypj only supports unix system."
    FAILED_GET_POETRY_VER = "Failed to get poetry version."
    FAILED_POETRY_NEW = "Failed to 'poetry new'."
    FAILED_POETRY_CONFIG = "Failed to configure poetry."
    FAILED_POETRY_ADD = "Failed to add package via poetry."
    RESOURCE_NOT_FOUND = "Resource does not exist. Please report this issue."
    PACKAGE_NOT_FOUND = "The target package does not exist."

    def __str__(self) -> str:
        return self.name


class PypjError(Exception):
    def __init__(self, message: Emsg):
        self.message = message.value
        super().__init__(self.message)
