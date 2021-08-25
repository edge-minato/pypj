from subprocess import PIPE, CompletedProcess, run

from .const import Emoji
from .exception import Emsg, PypjError
from .setting import PypjSetting


def command(cmd: str) -> CompletedProcess:

    print(f"  Command: {cmd} {Emoji.WAIT}", end="", flush=True)
    r = run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    status = Emoji.OK if r.returncode == 0 else Emoji.NG
    print(f"\r  Command: {cmd} {status}", flush=True)
    return r


def poetry_new(setting: PypjSetting) -> None:
    POETRY_NEW_CMD = f"poetry new {setting.package_name}"
    if setting.src_flag:
        POETRY_NEW_CMD += " --src"
    r = command(POETRY_NEW_CMD)
    if r.returncode != 0:
        raise PypjError(Emsg.FAILED_POETRY_NEW)
    VENV_IN_PJ_CMD = f"poetry config virtualenvs.in-project {str(setting.venv_in_pj).lower()}"
    r = command(VENV_IN_PJ_CMD)
    if r.returncode != 0:
        raise PypjError(Emsg.FAILED_POETRY_CONFIG)
    print(f"Initialize done {Emoji.LETS_GO}")


def poetry_add(setting: PypjSetting) -> None:
    ADD_CMD = "poetry add -D {}"
    command_list = [
        ADD_CMD.format(setting.formatter),
        ADD_CMD.format(setting.linter),
        ADD_CMD.format(setting.type_linter),
        ADD_CMD.format(setting.import_formatter),
        ADD_CMD.format(setting.test_fw),
    ]
    for plugin in setting.plugin:
        command_list.append(ADD_CMD.format(plugin))
    for cmd in command_list:
        r = command(cmd)
        if r.returncode != 0:
            raise PypjError(Emsg.FAILED_POETRY_ADD)
