
import pygame
from md3v_snake.view.game_board import GameBoard
import md3v_snake.consts as consts

class StartupMenu:
    def __init__( self, config, assets, screen ):
        self.assets = assets
        self.screen = screen

    def check_start_button(self, mouse):
        if consts.START_BUT_REC[1] > mouse[0] > consts.START_BUT_REC[0] \
        and consts.START_BUT_REC[3] > mouse[1] > consts.START_BUT_REC[2]:
            return True
        return False

    def check_options_button(self, mouse):
        if consts.START_BUT_REC[1] > mouse[0] > consts.START_BUT_REC[0] \
        and consts.START_BUT_REC[3] > mouse[1] > consts.START_BUT_REC[2]:
            return True
        return False

    def show_startup_menu( self ):
        self.screen.blit(self.assets.get_background_asset(), (0, 0))
        self.screen.blit(self.assets.get_start_asset(), (355, 100))
        self.screen.blit(self.assets.get_options_asset(), (355, 250))
        pygame.display.update()
