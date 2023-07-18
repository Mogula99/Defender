"""
This module tests the DirectionVector class
"""

import pytest

from app.utils.direction_vector import DirectionVector
from app.utils.position import Position


@pytest.mark.parametrize(
    'direction_vector, expected_tuple',
    [
        (DirectionVector(0, 0), (0, 0)),
        (DirectionVector(80, 0), (1, 0)),
        (DirectionVector(4, 3), (0.8, 0.6)),
    ])
def test_get_tuple(direction_vector: DirectionVector, expected_tuple: tuple[float, float]):
    """
    This function tests the get_tuple() method of the DirectionVector class
    :param direction_vector: DirectionVector to test
    :param expected_tuple: Expected result
    :return:
    """
    assert direction_vector.get_tuple() == expected_tuple


def test_create_vector():
    """
    This function tests the create_vector() method of the DirectionVector class
    """
    start_position: Position = Position(0, 0)
    end_position: Position = Position(1024, 0)

    expected_vector: DirectionVector = DirectionVector(1, 0)

    vector: DirectionVector = DirectionVector.create_vector(start_position, end_position)

    assert vector.xCoord == expected_vector.xCoord
    assert vector.yCoord == expected_vector.yCoord
