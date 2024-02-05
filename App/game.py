import pygame
from settings import Settings
from trap import Trap
from food import Food
from object import Object
from player import Player

class Game(Settings):
    def __init__(self, level = 2, mode = 1):
        pygame.init()
        super().__init__()
        #Pygame
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))       
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 5000
        
        #Settings
        self.level = level
        self.mode = 1
        
        #Game
        self.game_started = True
        self.player = Player(self.screen)
        self.foods = []
        self.traps = []
        self.nb_foods = 5
        self.nb_traps = 2
        self.adapt_level()

            
    def play(self):
        while self.game_started:
            self.screen.fill("white")
            self.create_foods()
            self.create_traps()
            self.render_objects()
            self.player.move(self)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_started = False
            pygame.display.flip()       
        pygame.quit()
        
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

