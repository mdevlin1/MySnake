
import pygame
from md3v_snake.view.game_board import GameBoard
import md3v_snake.consts as consts

class StartupMenu:
    def __init__( self, config ):
        self.config = config

    def Start( self ):
        screen = pygame.display.set_mode((1000, 600))
        gameboard = GameBoard()

        # Initialize images 
        background = pygame.image.load(consts.GAME_BACKGROUND_ASSET).convert()
        start = pygame.image.load(consts.START_BUTTON_ASSET).convert()
        options = pygame.image.load(consts.OPTIONS_BUTTON_ASSET).convert()
        image = pygame.image.load(consts.SNAKE_SQUARE_ASSET).convert()
        speed = 300
    
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # Start button bounding rect
                if 645 > mouse[0] > 355 and 200 > mouse[1] > 100 and event.type == pygame.MOUSEBUTTONUP:
                        gameboard.Start()
                # Options button bounding rect
                elif 645 > mouse[0] > 355 and 350 > mouse[1] > 250 and event.type == pygame.MOUSEBUTTONUP:
                    screen.blit(background, (0, 0))
                    break

            screen.blit(background, (0, 0))
            screen.blit(start, (355, 100))
            screen.blit(options, (355, 250))
            pygame.display.update()
            pygame.time.delay(speed)
