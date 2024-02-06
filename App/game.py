from math import floor
import pygame
from recap_game import RecapGame
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
        self.start_time = pygame.time.get_ticks()
        # self.total_time = 120000
        self.total_time = 3000
    
    def run(self):
        while self.game_running:
            self.screen.fill((194, 161, 236))
            self.create_foods()
            self.create_traps()
            self.render_objects()
            self.player.move(self)
            self.game_running = self.pygame_event()
            self.diplay_timer()
            self.display_score()
            self.display_radius()
            self.display_speed()
            self.display_level()
            pygame.display.flip()
                    
    # ==== Subfunctions ==== #
    
    def diplay_timer(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        if(elapsed_time >= self.total_time):
            self.game_running = False
            recap = RecapGame(score = self.player.get_score(), screen = self.screen)
            recap.run()
        else:
            remaining_time = max((self.total_time - elapsed_time) // 1000, 0)
            font = pygame.font.Font(None, 36)  # Police de caractères et taille
            text_surface = font.render(f"Time: {remaining_time}", True, ((0,0,0)))  # Couleur rouge
            text_rect = text_surface.get_rect(topleft=(10, 10))  # Position en haut à gauche
            self.screen.blit(text_surface, text_rect)
        
    def display_score(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"Score: {floor(self.player.get_score())}", True, ((0,0,0)))
        text_rect = text_surface.get_rect(topleft=(10, 50))
        self.screen.blit(text_surface, text_rect)
        
    def display_radius(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"Radius: {floor(self.player.get_radius())}", True, ((0,0,0)))
        text_rect = text_surface.get_rect(topleft=(10, 90))
        self.screen.blit(text_surface, text_rect)
    
    def display_speed(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"Speed: {floor(self.player.get_speed())}", True, ((0,0,0)))
        text_rect = text_surface.get_rect(topleft=(10, 130))
        self.screen.blit(text_surface, text_rect)
    
    def display_level(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"Level: {self.get_key_from_value(self.alllevels, self.level)}", True, (0,0,0))
        text_rect = text_surface.get_rect(topleft=(10, 170))
        self.screen.blit(text_surface, text_rect)
    
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

