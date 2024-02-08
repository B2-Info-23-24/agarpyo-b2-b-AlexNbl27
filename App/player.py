from math import floor
import pygame
from settings import Settings
from object import Object


class Player(Object, Settings):
    def __init__(self, screen):
        Settings.__init__(self)
        _radius = 40
        _color = self.PLAYER_COLOR
        Object.__init__(self, _radius, _color, screen.get_width() // 2, screen.get_height() // 2)
        self.speed = 100
        self.score = 0

    def eat(self):
        self.score += 1
        self.increase_radius()
        self.increase_speed()
    
    def increase_radius(self):
        if(self.radius + 2 >= 200):
            self.radius = 200
        else :
            self.radius += 2
    
    def increase_speed(self):
        if(self.radius + 5 >= 500):
            self.speed = 500
        else :
            self.speed += 5
    
    def divide(self, level = 2):
        self.radius = self.radius / level
        self.speed = self.speed / level

    def get_score(self):
        return self.score

    def get_speed(self):
        return self.speed
    
    def get_radius(self):
        return self.radius
    
    def move(self, game):
        if(game.mode == game.allmodes["mouse"]):
            self.move_to_mouse(game.mypygame.dt)
        elif(game.mode == game.allmodes["keyboard"]):
            keys = pygame.key.get_pressed()
            self.key_pressed(game.mypygame.dt, keys)
        self.teleport(game.mypygame.screen)
        self.colisions(game)
    
    def teleport(self, screen):
        # Left
        if(self.x < 0):
            self.x = screen.get_width() - 1
        # Right
        elif(self.x > screen.get_width() - 1):
            self.x = 0
        # Up
        elif(self.y < 0):
            self.y = screen.get_height() - 1
        # Down
        elif(self.y > screen.get_height() - 1):
            self.y = 0
    
    def colisions(self, game):
        for trap in game.traps:
            if self.collide(trap):
                if(self.radius > trap.radius):
                    game.traps.remove(trap)
                    self.divide(game.level)
        for food in game.foods:
            if self.collide(food):
                game.foods.remove(food)
                self.eat()
    
    # ==== Keyboard mode ==== #
    
    def key_pressed(self, dt, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * dt
        if keys[pygame.K_UP]:
            self.y -= self.speed * dt
        if keys[pygame.K_DOWN]:
            self.y += self.speed * dt
            
    # ==== Mouse mode ==== #
            
    def move_to_mouse(self, dt):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = self.get_angle(mouse_x, mouse_y)
        self.x += self.speed * dt * angle[0]
        self.y += self.speed * dt * angle[1]
        
    def get_angle(self, mouse_x, mouse_y):
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        distance = (dx**2 + dy**2)**0.5 # T'as vu je connais Pythagore
        if floor(distance) > 0:
            dx /= distance
            dy /= distance
        else:
            dx = 0
            dy = 0
        return dx, dy           
    