import pygame
from checkboxes import MyCheckbox, MyCheckboxesGroup
from game import Game
from button import Button
from my_pygame import MyPygame
from settings import Settings

class Menu(Settings):
    def __init__(self, mypygame):
        Settings.__init__(self)
        self.mypygame = mypygame
        self.level_selected = 1
        self.mode = 1
        self.menu_running = True
        self.buttons = []
        self.groupCheckboxes = MyCheckboxesGroup()
        self.create_button()
        self.run()
        
    def run(self):
        while self.menu_running:
            if not pygame.display.get_init():
                break
            self.mypygame.screen.fill((194, 161, 236))
            self.render_menu()
            self.menu_running = self.mypygame.pygame_event(self.buttons, self.groupCheckboxes, p=pygame.K_p)
            if isinstance(self.menu_running, Button):
                self.getSettings()
                game = Game(self.mypygame, self.level_selected, self.mode)
                game.run()
            if isinstance(self.menu_running, str):
                if self.menu_running == "p":
                    self.getSettings()
                    game = Game(self.mypygame, self.level_selected, 2)
                    game.run()
            if pygame.display.get_init() and self.menu_running:
                pygame.display.flip()  
        pygame.quit()
        
    def getSettings(self):
        if(isinstance(self.menu_running, Button)):
            if(self.menu_running.text == "Play with mouse"):
                self.mode = 1
            elif(self.menu_running.text == "Play with keyboard"):
                self.mode = 2
        if(self.groupCheckboxes.get_selected() == "Easy mode"):
            self.level_selected = 2
        elif(self.groupCheckboxes.get_selected() == "Normal mode"):
            self.level_selected = 3
        elif(self.groupCheckboxes.get_selected() == "Hard mode"):
            self.level_selected = 4
                
    def create_button(self):
        button_width = 400
        button_height = 75
        button_color = self.WHITE
        font = pygame.font.SysFont(None, 30)
        button1 = Button(self.mypygame.screen, (self.mypygame.screen.get_width() - button_width) // 2, 200, button_width, button_height, button_color, "Play with mouse", self.BLACK, font)
        self.buttons.append(button1)
        button2 = Button(self.mypygame.screen, (self.mypygame.screen.get_width() - button_width) // 2, 300, button_width, button_height, button_color, "Play with keyboard", self.BLACK, font)
        self.buttons.append(button2)   
        checkbox1 = MyCheckbox(self.mypygame.screen, 100, 400, 20, 20, True, "Easy mode", self.BLACK, font)
        self.groupCheckboxes.checkboxes.append(checkbox1)
        checkbox2 = MyCheckbox(self.mypygame.screen, 100, 450, 20, 20, False, "Normal mode", self.BLACK, font)
        self.groupCheckboxes.checkboxes.append(checkbox2)
        checkbox3 = MyCheckbox(self.mypygame.screen, 100, 500, 20, 20, False, "Hard mode", self.BLACK, font)
        self.groupCheckboxes.checkboxes.append(checkbox3)
            
    def render_menu(self):
        for button in self.buttons:
            button.draw()
        for checkbox in self.groupCheckboxes.checkboxes:
            checkbox.draw()


