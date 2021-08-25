from pypj import cui

YES = ["y", "Y", "yes", "Yes", "YES"]
NO = ["n", "N", "no", "No", "NO"]


def test_is_yes() -> None:
    for r in YES:
        assert cui.is_yes(r)
    for r in NO:
        assert not cui.is_yes(r)
    assert not cui.is_yes("")


def test_is_no() -> None:
    for r in NO:
        assert cui.is_no(r)
    for r in YES:
        assert not cui.is_no(r)
    assert not cui.is_no("")


def test_is_yes_or_no() -> None:
    for r in YES:
        assert cui.is_yes_or_no(r)
    for r in NO:
        assert cui.is_yes_or_no(r)
    assert not cui.is_yes_or_no("aaa")
    assert not cui.is_yes_or_no("")


def test_is_empty() -> None:
    assert cui.is_empty("")
    assert not cui.is_empty("a")


def test_can_be_int() -> None:
    assert cui.can_be_int("1")
    assert not cui.can_be_int("")
    assert not cui.can_be_int("a")
