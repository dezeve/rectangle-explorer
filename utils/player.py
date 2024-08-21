import pygame

class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, tile_list, lava_group, finish_group,
                screen, is_game_over, is_game_finished):
        dx = 0
        dy = 0

        if is_game_over == False:
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                dx -= 5
            if key[pygame.K_RIGHT]:
                dx += 5
            if key[pygame.K_SPACE] and self.jumped == False:
                self.vel = -15
                self.jumped = True

            self.vel += 1
            if self.vel > 10:
                self.vel = 10
            dy += self.vel

            for tile in tile_list:
                if tile[1].colliderect(self.rect.x, self.rect.y + dy,
                                        self.width, self.height):
                    if self.vel < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel = 0
                    elif self.vel >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel = 0
                        self.jumped = False
                if tile[1].colliderect(self.rect.x + dx, self.rect.y,
                                        self.width, self.height):
                    dx = 0
                if pygame.sprite.spritecollide(self, lava_group, False):
                    is_game_over = True
                if pygame.sprite.spritecollide(self, finish_group, False):
                    is_game_finished = True

            self.rect.x += dx
            self.rect.y += dy

        screen.blit(self.image, self.rect)

        return is_game_over, is_game_finished
    
    def reset(self, x, y):
        player = pygame.Surface((20, 30))
        player.fill((20, 44, 92))
        self.image = player
        self.rect = player.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 0
        self.jumped = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()
