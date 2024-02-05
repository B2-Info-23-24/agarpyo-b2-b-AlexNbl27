import random
from object import Object


class Food(Object):
    def __init__(self, screen):
        _radius = 30
        _color = (0, 255, 0)
        _x = random.randint(2*_radius, screen.get_width() - 2*_radius)
        _y = random.randint(2*_radius, screen.get_height() + 2*_radius)
        super().__init__(_radius, _color, _x, _y)