YES = ["y", "Y", "yes", "Yes", "YES"]
NO = ["n", "N", "no", "No", "NO"]


def ask(msg: str) -> str:
    print(msg, end="")
    return input()


def is_yes(r: str) -> bool:
    return r in YES


def is_no(r: str) -> bool:
    return r in NO


def is_yes_or_no(r: str) -> bool:
    return is_yes(r) or is_no(r)


def is_empty(r: str) -> bool:
    return r == ""


def can_be_int(r: str) -> bool:
    try:
        int(r)
        return True
    except ValueError:
        return False


def ask_with_default(msg: str, default: str) -> str:
    r = ask(msg)
    return default if is_empty(r) else r


def ask_with_default_num(msg: str, default: int) -> int:
    r = ask(msg)
    if is_empty(r):
        return int(default)
    if can_be_int(r):
        return int(r)
    print("Invalid input, try again.")
    return ask_with_default_num(msg, default)


def ask_yn(msg: str, default: bool = False) -> bool:
    r = ask(msg)
    if is_empty(r):
        return default
    if not is_yes_or_no(r):
        print("Invalid input, try again.")
        return ask_yn(msg, default)
    return is_yes(r)


def ask_Yn(msg: str) -> bool:
    return ask_yn(msg, True)


def ask_yN(msg: str) -> bool:
    return ask_yn(msg, False)


def ask_no_empty(msg: str) -> str:
    r = ask(msg)
    return ask_no_empty(msg) if is_empty(r) else r
