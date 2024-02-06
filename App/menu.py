import pygame
from checkboxes import MyCheckbox, MyCheckboxesGroup
from checkbox import Checkbox
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
        self.groupCheckboxes = MyCheckboxesGroup()
        self.create_button()
        self.menu()
        
    def menu(self):
        while self.menu_running:
            self.screen.fill((0, 0, 0))
            self.render_menu()
            self.menu_running = self.pygame_event(self.buttons, self.groupCheckboxes)
            if isinstance(self.menu_running, Button):
                self.getSettings()
                self.menu_running = False
                game = Game(self.level_selected, self.mode)
                game.play()
                self.menu_running = True
                
    def getSettings(self):
        if(self.menu_running.text == "Jouer avec la souris"):
            self.mode = 1
        elif(self.menu_running.text == "Jouer avec le clavier"):
            self.mode = 2
        if(self.groupCheckboxes.get_selected() == "Mode facile"):
            self.level_selected = 2
        elif(self.groupCheckboxes.get_selected() == "Mode moyen"):
            self.level_selected = 3
        elif(self.groupCheckboxes.get_selected() == "Mode difficile"):
            self.level_selected = 4
                
    def create_button(self):
        button_width = 400
        button_height = 75
        button_color = (255, 255, 255)
        font = pygame.font.SysFont(None, 30)
        button1 = Button(self.screen, (self.screen.get_width() - button_width) // 2, 200, button_width, button_height, button_color, "Jouer avec la souris", (0, 0, 0), font)
        self.buttons.append(button1)
        button2 = Button(self.screen, (self.screen.get_width() - button_width) // 2, 300, button_width, button_height, button_color, "Jouer avec le clavier", (0, 0, 0), font)
        self.buttons.append(button2)   
        checkbox1 = MyCheckbox(self.screen, 100, 400, 20, 20, True, "Mode facile", (255, 255, 255), font)
        self.groupCheckboxes.checkboxes.append(checkbox1)
        checkbox2 = MyCheckbox(self.screen, 100, 450, 20, 20, False, "Mode moyen", (255, 255, 255), font)
        self.groupCheckboxes.checkboxes.append(checkbox2)
        checkbox3 = MyCheckbox(self.screen, 100, 500, 20, 20, False, "Mode difficile", (255, 255, 255), font)
        self.groupCheckboxes.checkboxes.append(checkbox3)
            
    def render_menu(self):
        for button in self.buttons:
            button.draw()
        for checkbox in self.groupCheckboxes.checkboxes:
            checkbox.draw()
        pygame.display.flip()



