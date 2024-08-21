import pygame

class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        finish_block = pygame.Surface((tile_size, tile_size))
        finish_block.fill((153, 255, 153))
        self.image = finish_block
        self.rect = finish_block.get_rect()
        self.rect.x = x
        self.rect.y = y
