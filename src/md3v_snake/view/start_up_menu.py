
import pygame
from md3v_snake.view.game_board import GameBoard
import md3v_snake.consts as consts

class StartupMenu:
    def __init__( self, config, assets, screen ):
        self.assets = assets
        self.speed = config[ consts.PLAYER_SPEED ]
        self.screen = screen

    def start( self ):
    
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # Start button bounding rect
                if consts.START_BUT_REC[1] > mouse[0] > consts.START_BUT_REC[0] \
                    and consts.START_BUT_REC[3] > mouse[1] > consts.START_BUT_REC[2] \
                    and event.type == pygame.MOUSEBUTTONUP:
                    return
                # Options button bounding rect
                elif consts.START_BUT_REC[1] > mouse[0] > consts.START_BUT_REC[0] \
                    and consts.START_BUT_REC[3] > mouse[1] > consts.START_BUT_REC[2] \
                    and event.type == pygame.MOUSEBUTTONUP:
                    self.screen.blit(self.assets.get_background_asset(), (0, 0))
                    break

            self.screen.blit(self.assets.get_background_asset(), (0, 0))
            self.screen.blit(self.assets.get_start_asset(), (355, 100))
            self.screen.blit(self.assets.get_options_asset(), (355, 250))
            pygame.display.update()
            # FIXME: Player speed is the same as time delay for updating screen?
            pygame.time.delay(self.speed)
