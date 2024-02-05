import pygame
from game import Game
from button import Button
from my_pygame import MyPygame
from settings import Settings

class Menu(Settings, MyPygame):
    def __init__(self):
        Settings.__init__(self)
        MyPygame.__init__(self)
        
        self.level_selected = 1
        self.mode = 1
        self.menu_running = True
        self.buttons = []
        self.create_button()
        self.menu()
        
    def menu(self):
        while self.menu_running:
            self.screen.fill((0, 0, 0))
            self.render_menu()
            self.menu_running = self.pygame_event(self.buttons)
            if isinstance(self.menu_running, Button):
                if(self.menu_running.text == "Jouer avec la souris"):
                    self.level_selected = 2
                    self.mode = 1
                elif(self.menu_running.text == "Jouer avec le clavier"):
                    self.level_selected = 2
                    self.mode = 2
                self.menu_running = False
                game = Game(self.level_selected, self.mode)
                game.play()
                self.menu_running = True 
                
    def create_button(self):
        button_width = 400
        button_height = 75
        button_color = (255, 255, 255)
        font = pygame.font.SysFont(None, 30)
        button1 = Button(self.screen, (self.screen.get_width() - button_width) // 2, 200, button_width, button_height, button_color, "Jouer avec la souris", (0, 0, 0), font)
        self.buttons.append(button1)
        button2 = Button(self.screen, (self.screen.get_width() - button_width) // 2, 300, button_width, button_height, button_color, "Jouer avec le clavier", (0, 0, 0), font)
        self.buttons.append(button2)
    
    def render_menu(self):
        for button in self.buttons:
            button.draw()
        pygame.display.flip()



