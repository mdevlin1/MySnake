import pygame
import md3v_snake.consts as consts

class GameBoard:
    def __init__( self, config, assets, screen ):
        self.assets = assets
        self.screen = screen

    def show_game_board( self, objective_pos, players ):
        self.screen.blit(self.assets.get_background_asset(), (0, 0))
        self.screen.blit(self.assets.get_image_asset(), players[0].position)
        self.screen.blit(self.assets.get_image_asset(), objective_pos)
        pygame.display.update()

    def update_player_pos( self, objective_pos, players ):
        for player in players:
            self.screen.blit(self.assets.get_clear_asset(), player.last_position)
            self.screen.blit(self.assets.get_image_asset(), player.position)

        self.screen.blit(self.assets.get_image_asset(), objective_pos)
        pygame.display.update()


    def update_player_speed( self, player_speed ):
        pygame.time.delay(player_speed)

    def get_screen_rect( self ):
        return self.screen.get_rect()