import pygame

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        lava_block = pygame.Surface((tile_size, tile_size))
        lava_block.fill((204, 0, 0))
        self.image = lava_block
        self.rect = lava_block.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_move_direction = 1
        self.x_move_counter = 0
        self.y_move_direction = -1
        self.y_move_counter = 0
    def update(self):
        self.rect.x += self.x_move_direction
        if self.x_move_counter >= 50:
            self.x_move_direction *= -1
            self.x_move_counter *= -1
        self.x_move_counter += 1
        self.rect.y += self.y_move_direction
        if self.y_move_counter >= 10:
            self.y_move_direction *= -1
            self.y_move_counter *= -1
        self.y_move_counter += 1
