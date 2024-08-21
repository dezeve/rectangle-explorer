import pygame

class Text():
    def __init__(self, text, font_size, color):
        font = pygame.font.Font(None, font_size)
        text = font.render(text, True, color)
        self.text = text
    def draw(self, x, y, screen):
        screen.blit(self.text, (x, y))
