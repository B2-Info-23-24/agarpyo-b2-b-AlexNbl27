import pygame

class Object():
    def __init__(self, radius, color = (0, 0, 0), x = 0, y = 0):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
    
    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
    def collide(self, object):
        distance = ((self.x - object.x)**2 + (self.y - object.y)**2)**0.5
        return distance < self.radius + object.radius