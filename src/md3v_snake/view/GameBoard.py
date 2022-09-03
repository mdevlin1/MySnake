import pygame
import random
import md3v_snake.consts as consts
from md3v_snake.model.Player import Player

class GameBoard:
    def __init__( self ):
        pass

    def Start( self ):
        # setup display and load images
        screen = pygame.display.set_mode((1000, 600))
        image = pygame.image.load(consts.SNAKE_SQUARE_ASSET).convert()
        clear = pygame.image.load(consts.CLEAR_SCREEN_ASSET).convert()
        background = pygame.image.load(consts.GAME_BACKGROUND_ASSET).convert()

        notOver = True
        p1 = Player()
        players = [p1]
        objective_pos = [random.randrange(0, 1000, 20), random.randrange(0, 600, 20)]
                
        screen.blit(background, (0, 0))
        screen.blit(image, players[0].position)
        screen.blit(image, objective_pos)
        pygame.display.update()

        # default change
        change_in_position = (0, 20)
        speed = 300

        while notOver:
            # Entire board game is full
            if len(players) == 80:
                notOver = False
                self.youWin()
            
            screen.blit(clear, players[0].position)
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


            # When out of bounds, go to opposite side of board
            if players[0].position[0] >= 1000:
                players[0].position[0] = 0
            elif players[0].position[0] < 0:
                players[0].position[0] = 1000

            if players[0].position[1] >= 600:
                players[0].position[1] = 0
            elif players[0].position[1] < 0:
                players[0].position[1] = 600

            # objective player reached
            if players[0].position == objective_pos:
                screen.blit(clear, objective_pos)
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
                if speed > 75:
                    speed -= 4

            for i in range(1, len(players)):
                players[i].last_position = players[i].position
                screen.blit(clear, players[i].position)
                players[i].position = players[i-1].last_position
                screen.blit(image, players[i].position)

            if self.inList(players, players[0]):
                notOver = False
                self.game_over()

            screen.blit(image, players[0].position)
            screen.blit(image, objective_pos)
            pygame.display.update()
            pygame.time.delay(speed)

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
