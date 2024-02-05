import pygame
from object import Object


class Player(Object):
    def __init__(self, screen): 
        _radius = 40
        _color = (255, 0, 0)
        super().__init__(_radius, _color, screen.get_width() // 2, screen.get_height() // 2)
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
    
    def move(self, game):
        if(game.mode == game.allmodes["mouse"]):
            self.move_to_mouse(game)
        elif(game.mode == game.allmodes["keyboard"]):
            keys = pygame.key.get_pressed()
            self.key_pressed(game.dt, keys)
        self.teleport(game.screen)
        self.colisions(game)
    
    def teleport(self, screen):
        if(self.x > screen.get_width()):
            self.x = 0
        if(self.x < 0):
            self.x = screen.get_width()
        if(self.y > screen.get_height()):
            self.y = 0
        if(self.y < 0):
            self.y = screen.get_height()
    
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
            
    def move_to_mouse(self, game):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        distance = (dx**2 + dy**2)**0.5 # T'as vu je connais pythagore
        if distance > 0:
            self.x += self.speed * dx / distance * game.dt
            self.y += self.speed * dy / distance * game.dt