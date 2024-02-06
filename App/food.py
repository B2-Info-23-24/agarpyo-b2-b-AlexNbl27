import random
from settings import Settings
from object import Object


class Food(Object, Settings):
    def __init__(self, screen):
        Settings.__init__(self)
        _radius = 30
        _color = self.FOOD_COLOR
        _x = random.randint(2*_radius, screen.get_width() - 2*_radius)
        _y = random.randint(2*_radius, screen.get_height() - 2*_radius)
        Object.__init__(self, _radius, _color, _x, _y)