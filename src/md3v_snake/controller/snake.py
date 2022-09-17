
from md3v_snake.view.start_up_menu import StartupMenu
from md3v_snake.view.game_board import GameBoard
from md3v_snake.model.assets import Assets
from md3v_snake.config.load_config import load as conf_load
import md3v_snake.consts as consts
import pygame

class Snake:
    def __init__( self, config_file ):

        self.config = conf_load( config_file )
        self.speed = self.config[consts.PLAYER_SPEED]
        
        # setup display and load images
        # TODO: We should probably have the view objects initialise the screen,
        # but it must be initialized before loading assets
        screen = pygame.display.set_mode(
            (self.config[consts.SCREEN_X], 
            self.config[consts.SCREEN_Y])
        )

        # Load up images and sprites necessary for game
        assets = Assets()
        assets.load_assets( self.config[ consts.ASSET_DIR] )

        self.start_up_menu = StartupMenu( self.config, assets, screen )
        self.game_board = GameBoard( self.config, assets, screen )

    def run( self ):    
        self.start_up_menu.show_startup_menu()
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.start_up_menu.check_start_button( mouse ):
                        self.game_board.start()
                    if self.start_up_menu.check_options_button( mouse ):
                        return
            # FIXME: Player speed is the same as time delay for updating screen?
            pygame.time.delay(self.speed)

