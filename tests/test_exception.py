from pypj import Emsg, PypjError


def test_PypjError() -> None:
    try:
        raise PypjError(Emsg.OS_NOT_SUPPORTED)
    except PypjError as e:
        assert Emsg(str(e)) is Emsg.OS_NOT_SUPPORTED
