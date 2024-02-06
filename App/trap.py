import random
from settings import Settings
from object import Object


class Trap(Object, Settings):
    def __init__(self, screen):
        Settings.__init__(self)
        _radius = random.randint(40, 150)
        _color = self.TRAP_COLOR
        _x = random.randint(0, screen.get_width())
        _y = random.randint(0, screen.get_height())
        Object.__init__(self, _radius, _color, _x, _y)