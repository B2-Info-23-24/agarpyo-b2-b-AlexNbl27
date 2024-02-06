from math import floor
import pygame
from recap_game import RecapGame
from my_pygame import MyPygame
from settings import Settings
from trap import Trap
from food import Food
from player import Player

class Game(Settings):
    def __init__(self, mypygame, level = 2, mode = 1):
        Settings.__init__(self)
        self.mypygame = mypygame
        #Settings
        self.level = level
        self.mode = mode
        #Game
        self.game_running = True
        self.player = Player(self.mypygame.screen)
        self.foods = []
        self.traps = []
        self.nb_foods = 5
        self.nb_traps = 2
        self.adapt_level()
        self.start_time = pygame.time.get_ticks()
        self.total_time = 60000
        # self.total_time = 3000
    
    def run(self):
        while self.game_running:
            if not pygame.display.get_init():
                break
            self.mypygame.screen.fill(self.BACKGROUND)
            self.create_traps()
            self.create_foods()
            self.render_objects()
            self.display_stats()
            self.player.move(self)
            self.game_running = self.mypygame.pygame_event()
            if(self.game_running):
                self.diplay_timer()
                if pygame.display.get_init():
                    pygame.display.flip()
        
    # ==== Subfunctions ==== #  
    def diplay_timer(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        if(elapsed_time >= self.total_time):
            self.game_running = False
            recap = RecapGame(self.mypygame, score = self.player.get_score(), screen = self.mypygame.screen)
            recap.run()
        else:
            remaining_time = max((self.total_time - elapsed_time) // 1000, 0)
            font = pygame.font.Font(None, 36)
            text_surface = font.render(f"Time: {remaining_time}", True, self.BLACK)
            text_rect = text_surface.get_rect(topleft=(10, 10))
            self.mypygame.screen.blit(text_surface, text_rect)
        
    def display_stats(self):
        font = pygame.font.Font(None, 36)

        text_surface = font.render(f"Score: {floor(self.player.get_score())}", True, self.BLACK)
        text_rect = text_surface.get_rect(topleft=(10, 50))
        self.mypygame.screen.blit(text_surface, text_rect)

        text_surface = font.render(f"Radius: {floor(self.player.get_radius())}", True, self.BLACK)
        text_rect = text_surface.get_rect(topleft=(10, 90))
        self.mypygame.screen.blit(text_surface, text_rect)

        text_surface = font.render(f"Speed: {floor(self.player.get_speed())}", True, self.BLACK)
        text_rect = text_surface.get_rect(topleft=(10, 130))
        self.mypygame.screen.blit(text_surface, text_rect)

        text_surface = font.render(f"Level: {self.get_key_from_value(self.alllevels, self.level)}", True, self.BLACK)
        text_rect = text_surface.get_rect(topleft=(10, 170))
        self.mypygame.screen.blit(text_surface, text_rect)

    
    def create_foods(self):
        while(len(self.foods) < self.nb_foods):
            _food = Food(self.mypygame.screen)
            _isColliding = False
            for food in self.foods:
                if(_food.collide(food)):
                    _isColliding = True
                    break
            for trap in self.traps:
                if(_food.collide(trap)):
                    _isColliding = True
                    break
            if(not _isColliding):                   
                self.foods.append(_food)
    
    def create_traps(self):
        while(len(self.traps) < self.nb_traps):
            _trap = Trap(self.mypygame.screen)
            _isColliding = False
            for trap in self.traps:
                if(_trap.collide(trap)):
                    _isColliding = True
                    break
            for food in self.foods:
                if(_trap.collide(food)):
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
        self.player.render(self.mypygame.screen)
        for trap in self.traps:
            trap.render(self.mypygame.screen)
        for food in self.foods:
            food.render(self.mypygame.screen)

