from workflow import format_message


def test_format_message() -> None:
    assert format_message("union") == "ok: union"
