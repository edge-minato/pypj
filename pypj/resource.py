import pkgutil
from pathlib import Path

from .exception import Emsg, PypjError


def get_resource(package_name: str, resource_file: Path) -> str:
    try:
        resource = pkgutil.get_data(package_name, str(resource_file))
        if resource is None:
            raise PypjError(Emsg.RESOURCE_NOT_FOUND)
        return resource.decode("utf-8")
    except FileNotFoundError:
        raise PypjError(Emsg.RESOURCE_NOT_FOUND)


def get_my_resource(resource_file: str) -> str:
    return get_resource(__package__, Path("resources").joinpath(resource_file))
