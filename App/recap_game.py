import pygame
from settings import Settings
from button import Button
from my_pygame import MyPygame

class RecapGame(Settings):
    def __init__(self, mypygame, **kwargs):
        Settings.__init__(self)
        self.mypygame = mypygame
        self.score = kwargs.get("score")
        self.mypygame.screen = kwargs.get("screen")
        self.recap_running = True
        _width = 400
        _x = self.mypygame.screen.get_width() // 2 - _width // 2
        _y = self.mypygame.screen.get_height() // 2 - _width // 3
        self.buttons = [Button(self.mypygame.screen, _x, _y, _width, 50, (0, 0, 255), "Retourner à l'accueil", self.WHITE, pygame.font.Font(None, 36))]

    def run(self):
        while self.recap_running:
            if not pygame.display.get_init():
                break
            self.mypygame.screen.fill(self.BACKGROUND)
            self.display_result()
            for button in self.buttons:
                button.draw()
            self.recap_running = self.mypygame.pygame_event(self.buttons)
            if isinstance(self.recap_running, Button):
                self.recap_running = False
            if self.recap_running and pygame.display.get_init():
                pygame.display.flip()

    def display_result(self):
        font = pygame.font.Font(None, 36)
        
        winning_sentence = "Congratulations! You did a great job!" if self.score >= 80 else "You can do better! Try again!"
        
        text_surface_score = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_surface_winning = font.render(winning_sentence, True, (0, 0, 0))
        
        text_rect_score = text_surface_score.get_rect(center=(self.mypygame.screen.get_width() // 2, 100))
        text_rect_winning = text_surface_winning.get_rect(center=(self.mypygame.screen.get_width() // 2, 150))

        self.mypygame.screen.blit(text_surface_score, text_rect_score)
        self.mypygame.screen.blit(text_surface_winning, text_rect_winning)
