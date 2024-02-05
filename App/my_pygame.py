import pygame
from button import Button


class MyPygame:
    def __init__(self):
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))       
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 5000
        
    def pygame_event(self, buttons = []):
        event_running = True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                event_running = False
            if event.type == pygame.QUIT:
                event_running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                _index = 0
                for button in buttons:
                    if button.is_clicked(event):
                        return button
                    _index += 1                 
        return event_running