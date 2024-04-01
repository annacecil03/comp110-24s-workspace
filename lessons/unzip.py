"""Splitting a dictionary into two lists."""


__author__: str = "730464679"


def get_keys(test: dict[str, int]) -> list[str]:
    """Writing function definition to get a list of keys."""
    x: list[str] = []
    for key in test:
        x.append(key)
    return x


def get_values(test: dict[str, int]) -> list[int]:
    """Writing function definition to obtain values."""
    y: list[int] = []
    for key in test:
        y.append(test[key])
    return y
