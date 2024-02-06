import pygame
from button import Button
from my_pygame import MyPygame

class RecapGame(MyPygame):
    def __init__(self, **kwargs):
        super().__init__()
        self.score = kwargs.get("score")
        self.screen = kwargs.get("screen")
        self.recap_running = True
        _width = 400
        _x = self.screen.get_width() // 2 - _width // 2
        _y = self.screen.get_height() // 2 - _width // 3
        self.buttons = [Button(self.screen, _x, _y, _width, 50, (0, 0, 255), "Retourner à l'accueil", (255, 255, 255), pygame.font.Font(None, 36))]

    def run(self):
        while self.recap_running:
            self.screen.fill((194, 161, 236))
            self.display_result()
            for button in self.buttons:
                button.draw()
            self.recap_running = self.pygame_event(self.buttons)
            if isinstance(self.recap_running, Button):
                self.recap_running = False
            pygame.display.flip()

    def display_result(self):
        font = pygame.font.Font(None, 36)
        
        # Add a winning sentence based on the score
        if self.score >= 80:
            winning_sentence = "Congratulations! You did a great job!"
        else:
            winning_sentence = "You can do better! Try again!"

        text_surface_score = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_surface_winning = font.render(winning_sentence, True, (0, 0, 0))

        text_rect_score = text_surface_score.get_rect(center=(self.screen.get_width() // 2, 100))
        text_rect_winning = text_surface_winning.get_rect(center=(self.screen.get_width() // 2, 150))

        self.screen.blit(text_surface_score, text_rect_score)
        self.screen.blit(text_surface_winning, text_rect_winning)
