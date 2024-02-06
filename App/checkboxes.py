import pygame

class MyCheckbox:
    def __init__(self, surface, x, y, width, height, selected, text, text_color, font):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)
        self.selected = selected
        self.text = text
        self.text_color = text_color
        self.font = font
        self.check_font = pygame.font.Font(None, 36)  # Font for the check symbol
    
    def draw(self):
        # Draw the checkbox rectangle
        if self.selected:
            pygame.draw.rect(self.surface, (0, 0, 255), self.rect)
        else:
            pygame.draw.rect(self.surface, (255, 255, 255), self.rect)
        
        check_symbol = 'X' if self.selected else ''  # Display 'X' if selected, else ''
        check_surface = self.check_font.render(check_symbol, True, (255, 255, 255))
        check_rect = check_surface.get_rect(center=(self.rect.left + 20, self.rect.centery))  # Adjust position
        
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(midleft=(self.rect.left + 40, self.rect.centery))
        
        self.surface.blit(check_surface, check_rect)
        self.surface.blit(text_surface, text_rect)
        
    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.selected = not self.selected
            return True
        return False
    
class MyCheckboxesGroup:
    def __init__(self, checkboxes = []):
        self.checkboxes = checkboxes
    
    def draw(self):
        for checkbox in self.checkboxes:
            checkbox.draw()
            
    def only_one_selected(self, checkbox):
        for _checkbox in self.checkboxes:
            if _checkbox != checkbox:
                _checkbox.selected = False
    
    def is_clicked(self):
        for checkbox in self.checkboxes:
            if checkbox.is_clicked():
                self.only_one_selected(checkbox)
                self.current_checkbox = checkbox
                return checkbox
            
    def get_selected(self):
        for checkbox in self.checkboxes:
            if checkbox.selected:
                return checkbox.text
        return None