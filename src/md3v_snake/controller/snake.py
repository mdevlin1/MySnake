
from md3v_snake.view.start_up_menu import StartupMenu
from md3v_snake.view.game_board import GameBoard
from md3v_snake.model.assets import Assets
from md3v_snake.config.load_config import load as conf_load
import md3v_snake.consts as consts
import pygame
from md3v_snake.model.player import Player
import random

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
        self.start_up = False
        self.running = False

        self.player_speed = self.config[consts.PLAYER_SPEED]

    def run( self ):    
        self.start_up_menu.show_startup_menu()
        self.start_up = True

        p1 = Player()
        players = [p1]
        objective_pos = [random.randrange(0, 1000, 20), random.randrange(0, 600, 20)]
        # default change
        change_in_position = (0, 20)

        while self.start_up:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.start_up_menu.check_start_button( mouse ):
                        self.game_board.show_game_board( objective_pos, players)
                        self.start_up = False
                    if self.start_up_menu.check_options_button( mouse ):
                        # TODO: Implement an options menu for changing configurable options, etc...
                        self.start_up = False
            # FIXME: Player speed is the same as time delay for updating screen?
            pygame.time.delay(self.speed)
        
        self.running = True
        while self.running:
            # Entire board game is full
            # Todo: Locked into screen size
            if len(players) == 80:
                self.running = False
                self.youWin()

            for event in pygame.event.get():
                # Quit game when exit button is pressed
                if event.type == pygame.QUIT:
                    notOver = False
                    self.game_over()

                # Alter direction of players move
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if change_in_position != (0, 20):
                            change_in_position = (0, -20)
                    elif event.key == pygame.K_DOWN:
                        if change_in_position != (0, -20):
                            change_in_position = (0, 20)
                    elif event.key == pygame.K_RIGHT:
                        if change_in_position != (-20, 0):
                            change_in_position = (20, 0)
                    elif event.key == pygame.K_LEFT:
                        if change_in_position != (20, 0):
                            change_in_position = (-20, 0)

            # record last position and change player's current position 
            players[0].last_position = players[0].position
            players[0].position = list(map(sum, zip(players[0].position, change_in_position)))

            self.checkScreenLimits( players[0] )

            # objective player reached
            if players[0].position == objective_pos:
                objective_pos = [random.randrange(0, 1000, 20), random.randrange(0, 600, 20)]
                while True:
                    elem_in_list = False
                    for i in range(0, len(players)):
                        if players[i].position == objective_pos:
                            objective_pos = [random.randrange(0, 1000, 20), random.randrange(0, 600, 20)]
                            elem_in_list = True
                            break
                        elem_in_list = False
                    
                    if elem_in_list == False:
                        break

                p2 = Player()
                players.append(p2)
                if self.player_speed > 75:
                    self.player_speed -= 4

            for i in range(1, len(players)):
                players[i].last_position = players[i].position
                players[i].position = players[i-1].last_position

            if self.inList(players, players[0]):
                notOver = False
                self.game_over()

            self.game_board.update_player_pos( objective_pos, players )
            # FIXME: Player speed is the same as time delay for updating screen?
            self.game_board.update_player_speed( self.player_speed )

    def checkScreenLimits( self, player ):
        # Get the screen dimensions which act as boundaries for
        # the snake "player"
        screen_rect = self.game_board.get_screen_rect()
        screen_x_boundary = screen_rect[2]
        screen_y_boundary = screen_rect[3]

        if player.position[consts.X_POS_IDX] >= screen_x_boundary:
            player.position[consts.X_POS_IDX] = 0
        elif player.position[consts.X_POS_IDX] < 0:
            player.position[consts.X_POS_IDX] = screen_x_boundary

        if player.position[consts.Y_POS_IDX] >= screen_y_boundary:
            player.position[consts.Y_POS_IDX] = 0
        elif player.position[consts.Y_POS_IDX] < 0:
            player.position[consts.Y_POS_IDX] = screen_y_boundary
    
    def inList(self, a, x):
        for i in range(1, len(a)):
            if a[i].position == x.position:
                    return True
        return False

    def game_over(self):
        pygame.quit()

    def youWin(self):
        print("you win!")
        pygame.quit()
