import random
from object import Object


class Trap(Object):
    def __init__(self, screen):
        _radius = random.randint(40, 150)
        _color = (109, 120, 200)
        _x = random.randint(0, screen.get_width())
        _y = random.randint(0, screen.get_height())
        super().__init__(_radius, _color, _x, _y)