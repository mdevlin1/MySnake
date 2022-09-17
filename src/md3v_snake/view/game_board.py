import pygame
import random
import md3v_snake.consts as consts
from md3v_snake.model.player import Player

class GameBoard:
    def __init__( self, config, assets, screen ):
        self.assets = assets
        self.screen = screen
        self.player_speed = config[ consts.PLAYER_SPEED ]
        self.running = False

    def start( self ):

        self.running = True
        p1 = Player()
        players = [p1]
        objective_pos = [random.randrange(0, 1000, 20), random.randrange(0, 600, 20)]
                
        self.screen.blit(self.assets.get_background_asset(), (0, 0))
        self.screen.blit(self.assets.get_image_asset(), players[0].position)
        self.screen.blit(self.assets.get_image_asset(), objective_pos)
        pygame.display.update()

        # default change
        change_in_position = (0, 20)

        while self.running:
            # Entire board game is full
            # Todo: Locked into screen size
            if len(players) == 80:
                self.running = False
                self.youWin()
            
            self.screen.blit(self.assets.get_clear_asset(), players[0].position)
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
                self.screen.blit(self.assets.get_clear_asset(), objective_pos)
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
                self.screen.blit(self.assets.get_clear_asset(), players[i].position)
                players[i].position = players[i-1].last_position
                self.screen.blit(self.assets.get_image_asset(), players[i].position)

            if self.inList(players, players[0]):
                notOver = False
                self.game_over()

            self.screen.blit(self.assets.get_image_asset(), players[0].position)
            self.screen.blit(self.assets.get_image_asset(), objective_pos)
            pygame.display.update()
            # FIXME: Player speed is the same as time delay for updating screen?
            pygame.time.delay(self.player_speed)

    def checkScreenLimits( self, player ):
        # Get the screen dimensions which act as boundaries for
        # the snake "player"
        screen_x_boundary = self.screen.get_rect()[2]
        screen_y_boundary = self.screen.get_rect()[3]

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
