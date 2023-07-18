"""
This module tests the Position class
"""

import pytest

from app.utils.position import Position


@pytest.mark.parametrize(
    'position, expected_tuple',
    [
        (Position(0, 0), (0, 0)),
        (Position(1248, 8421), (1248, 8421)),
        (Position(-4, -3), (-4, -3)),
    ])
def test_get_tuple(position: Position, expected_tuple: tuple[float, float]):
    """
    This function tests the get_tuple() method of Position class
    :param position: Position to test
    :param expected_tuple: Expected tuple
    """
    assert position.get_tuple() == expected_tuple


@pytest.mark.parametrize(
    'start, end, expected',
    [
        (Position(0, 0), Position(10, 0), 10),
        (Position(-150, 150), Position(-150, 155), 5),
        (Position(0, 0), Position(10, 10), 14.142135623730951)
    ])
def test_count_distance(start: Position, end: Position, expected: float):
    """
    This function tests the count_distance() method of Position class
    :param start: Position representing one end of the counted distance
    :param end: Position representing the other end of the counted distance
    :param expected: Expected result
    """
    assert Position.count_distance(start, end) == expected
