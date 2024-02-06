import pygame
from checkboxes import MyCheckboxesGroup
from button import Button


class MyPygame:
    def __init__(self):
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))       
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000
        
    def pygame_event(self, *args, **others_keys):
        event_running = True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    event_running = False
                if event.key == pygame.K_q:
                    event_running = False
                    pygame.quit()
                for key, value in others_keys.items():
                    if event.key == value:
                        return key
            elif event.type == pygame.QUIT:
                event_running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for arg in args:
                    if isinstance(arg, list):
                        for item in arg:
                            if item.is_clicked():
                                return item
                    elif isinstance(arg, MyCheckboxesGroup):
                        arg.is_clicked()
        return event_running
