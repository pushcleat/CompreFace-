from typing import List, Tuple

import attr

from src.services.dto.json_encodable import JSONEncodable


# noinspection PyUnresolvedReferences
@attr.s(auto_attribs=True, frozen=True)
class BoundingBox(JSONEncodable):
    """
    >>> BoundingBox(x_min=10, x_max=0, y_min=100, y_max=200, probability=0.5)
    Traceback (most recent call last):
    ...
    ValueError: 'x_min' must be smaller than 'x_max'
    """
    x_min: int = attr.ib(converter=int)
    y_min: int = attr.ib(converter=int)
    x_max: int = attr.ib(converter=int)
    y_max: int = attr.ib(converter=int)
    probability: float = attr.ib(converter=float)

    @x_min.validator
    def check_x_min(self, attribute, value):
        if value > self.x_max:
            raise ValueError("'x_min' must be smaller than 'x_max'")

    @y_min.validator
    def check_y_min(self, attribute, value):
        if value > self.y_max:
            raise ValueError("'y_min' must be smaller than 'y_max'")

    @probability.validator
    def check_probability(self, attribute, value):
        if not (0 <= value <= 1):
            raise ValueError("'probability' must be between 0 and 1")

    @property
    def xy(self):
        return (self.x_min, self.y_min), (self.x_max, self.y_max)

    def similar(self, other: 'BoundingBox', tolerance: int):
        """
        >>> BoundingBox(50,50,100,100,1).similar(BoundingBox(50,50,100,100,1),5)
        True
        >>> BoundingBox(50,50,100,100,1).similar(BoundingBox(50,50,100,95,1),5)
        True
        >>> BoundingBox(50,50,100,100,1).similar(BoundingBox(50,50,100,105,1),5)
        True
        >>> BoundingBox(50,50,100,100,1).similar(BoundingBox(50,50,100,94,1),5)
        False
        >>> BoundingBox(50,50,100,100,1).similar(BoundingBox(50,50,100,106,1),5)
        False
        """
        return (abs(self.x_min - other.x_min) <= tolerance
                and abs(self.y_min - other.y_min) <= tolerance
                and abs(self.x_max - other.x_max) <= tolerance
                and abs(self.y_max - other.y_max) <= tolerance)

    def similar_to_any(self, others: List['BoundingBox'], tolerance: int):
        """
        >>> BoundingBox(50,50,100,100,1).similar_to_any([BoundingBox(50,50,100,105,1),BoundingBox(50,50,100,106,1)],5)
        True
        >>> BoundingBox(50,50,100,100,1).similar_to_any([BoundingBox(50,50,100,106,1),BoundingBox(50,50,100,106,1)],5)
        False
        """
        for other in others:
            if self.similar(other, tolerance):
                return True
        return False

    def is_point_inside(self, xy: Tuple[int, int]):
        """
        >>> BoundingBox(100,700,150,750,1).is_point_inside((125,725))
        True
        >>> BoundingBox(100,700,150,750,1).is_point_inside((5,5))
        False
        """
        x, y = xy
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max
