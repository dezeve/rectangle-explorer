import pygame
import utils.constants
import utils.grid
import utils.player
import utils.button
import utils.text

pygame.init()

screen = pygame.display.set_mode((utils.constants.HORIZONTAL_RESOLUTION,
                                   utils.constants.VERTICAL_RESOLUTION))
clock = pygame.time.Clock()
pygame.display.set_caption(utils.constants.GAME_NAME)
running = True

[tile_list, lava_group, finish_group
 ] = utils.grid.build_tile_list(utils.constants.TILE_SIZE)
player = utils.player.Player(90, 530)
restart_button = utils.button.Button(
    utils.constants.HORIZONTAL_RESOLUTION // 2 - 75, 
    utils.constants.VERTICAL_RESOLUTION // 2 - 50, 
    "Restart", 50)
play_button = utils.button.Button(
    utils.constants.HORIZONTAL_RESOLUTION // 2 - 75, 
    utils.constants.VERTICAL_RESOLUTION // 2 - 50, 
    "Play", 50)
exit_button = utils.button.Button(
    utils.constants.HORIZONTAL_RESOLUTION // 2 - 75, 
    utils.constants.VERTICAL_RESOLUTION // 2 + 25, 
    "Exit", 50)
menu_button = utils.button.Button(
    utils.constants.HORIZONTAL_RESOLUTION // 2 - 75, 
    utils.constants.VERTICAL_RESOLUTION // 2 + 25, 
    "Go to Menu", 35)
menu_title = utils.text.Text("rectangle-explorer", 100, "blue")
finish_text = utils.text.Text("Thank You for Playing!", 75, "red")

is_game_over = False
is_game_finished = False

show_menu = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           is_clicked = True
    
    screen.fill((230, 255, 255))

    if show_menu:
      utils.text.Text.draw(menu_title, 90, 120, screen)
      if utils.button.Button.draw(play_button, screen
                                  ) and is_clicked:
         show_menu = False
      if utils.button.Button.draw(exit_button, screen
                                  ) and is_clicked:
         running = False
    elif is_game_finished:
        utils.text.Text.draw(finish_text, 110, 120, screen)
        if utils.button.Button.draw(restart_button, screen
                                    ) and is_clicked:
            utils.player.Player.reset(player, 90, 530)
            is_game_finished = False
        if utils.button.Button.draw(menu_button, screen
                                    ) and is_clicked:
            utils.player.Player.reset(player, 90, 530)
            is_game_finished = False
            show_menu = True            
    else:
      utils.grid.draw_level(tile_list, screen)
      finish_group.draw(screen)
      lava_group.draw(screen)
      lava_group.update()
      is_game_over, is_game_finished = utils.player.Player.update(
          player, tile_list, lava_group,
            finish_group, screen, is_game_over, is_game_finished)
      
      if is_game_over:
          if utils.button.Button.draw(restart_button, screen
                                      ) and is_clicked:
              utils.player.Player.reset(player, 90, 530)
              is_game_over = False
          if utils.button.Button.draw(menu_button, screen
                                      ) and is_clicked:
              utils.player.Player.reset(player, 90, 530)
              is_game_over = False
              show_menu = True

    is_clicked = False

    pygame.display.flip()

    clock.tick(utils.constants.MAX_FPS)

pygame.quit()
