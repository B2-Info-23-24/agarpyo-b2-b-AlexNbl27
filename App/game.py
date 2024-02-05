import pygame
from my_pygame import MyPygame
from settings import Settings
from trap import Trap
from food import Food
from player import Player

class Game(Settings, MyPygame):
    def __init__(self, level = 2, mode = 1):
        Settings.__init__(self)
        MyPygame.__init__(self)   
        #Settings
        self.level = level
        self.mode = mode
        #Game
        self.game_running = True
        self.player = Player(self.screen)
        self.foods = []
        self.traps = []
        self.nb_foods = 5
        self.nb_traps = 2
        self.adapt_level()
    
    def play(self):
        while self.game_running:
            self.screen.fill("white")
            self.create_foods()
            self.create_traps()
            self.render_objects()
            self.player.move(self)
            self.game_running = self.pygame_event()
            pygame.display.flip()
                    
    # ==== Subfunctions ==== #
    def create_foods(self):
        while(len(self.foods) < self.nb_foods):
            _food = Food(self.screen)
            _isColliding = False
            for food in self.foods:
                if(food.collide(_food)):
                    _isColliding = True
                    break
            for trap in self.traps:
                if(food.collide(_food)):
                    _isColliding = True
                    break
            if(not _isColliding):                   
                self.foods.append(_food)
    
    def create_traps(self):
        while(len(self.traps) < self.nb_traps):
            _trap = Trap(self.screen)
            _isColliding = False
            for trap in self.traps:
                if(trap.collide(_trap)):
                    _isColliding = True
                    break
            for food in self.foods:
                if(food.collide(_trap)):
                    _isColliding = True
                    break
            if(not _isColliding):
                self.traps.append(_trap)
    
    def adapt_level(self):
        if(self.level == 4):
            self.nb_foods = 2
            self.nb_traps = 4
        elif(self.level == 3):
            self.nb_foods = 3
            self.nb_traps = 3 
    
    def render_objects(self):
        self.player.render(self.screen)
        for trap in self.traps:
            trap.render(self.screen)
        for food in self.foods:
            food.render(self.screen)

