"""Test my garden functions."""
from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


__author__: str = "730464679"


def test_add_by_kind_use_case() -> None:
    """First use case - adding a plant to a kind already known."""
    plants_by_kind: dict[str, list[str]] = {}
    plant_kind = "flowers"
    plant = "carnations"
    test = add_by_kind(plants_by_kind, plant_kind, plant)
    assert test == {"flowers": ["carnations"]}


def test_add_by_kind_edge_case() -> None:
    """First edge case - adding a plant to a new kind."""
    plants_by_kind = {}
    plant_kind = "flowers"
    plant = "carnations"
    test = add_by_kind(plants_by_kind, plant_kind, plant)
    assert test == {"flowers": ["carnations"]}


def test_add_by_date_use_case() -> None:
    """Second use case - adding a plant to a date already known."""
    plants_by_date = {"March": ["lettuce"]}
    month = "March"
    plant = "potatoes"
    test = add_by_date(plants_by_date, month, plant)
    assert test == {"March": ["lettuce", "potatoes"]}


def test_add_by_date_edge_case() -> None:
    """Second edge case - adding a plant to a new date."""
    plants_by_date = {}
    month = "March"
    plant = "tomatoes"
    test = add_by_date(plants_by_date, month, plant)
    assert test == {"March": ["tomatoes"]}


def test_lookup_by_kind_and_date_use_case() -> None:
    """Third use case - lookup plants by kind and date."""
    plants_by_kind = {"flowers": ["carnations", "lillies"]}
    plants_by_date = {"March": ["carnations", "roses"]}
    plant_kind = "flowers"
    month = "March"
    test = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, month)
    assert test == "flowers to plant in March: ['carnations']."


def test_lookup_by_kind_and_date_edge() -> None:
    """Third edge case - lookup dates with no known date or kind."""
    plants_by_kind: dict[str, list[str]] = {"flowers": ["carnations"]}
    plants_by_date: dict[str, list[str]] = {"March": ["potatoes"]}
    plant_kind: str = "flowers"
    month: str = "March"
    test = lookup_by_kind_and_date(plants_by_kind, plants_by_date, plant_kind, month)
    assert test == "No flowers to plant in March."
