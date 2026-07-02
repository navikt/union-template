from workflow import add_numbers


def test_add_numbers() -> None:
    assert add_numbers(a=2, b=3) == 5
