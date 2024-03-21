import pygame
from pygame.locals import *
from constant import *
from ball import Ball
from paddle import Paddle
from block import Block, Wall

class Game:
    def __init__(self):      
        # Initialise screen
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PyWallBreaker")

        # Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(BG_COLOR)
        
        # Limit FPS with clock
        self.clock = pygame.time.Clock()

        #set the state of the game
        #"init" = stand by
        #"game" = after start throwing the ball and before the ball is out
        self.state = "init"

        # Initialise game objects (Ball, Paddle, Blocks)
        self.wall = Wall()
        self.paddle = Paddle()
        self.ball = Ball(self.paddle, self.wall)

    def init_state(self):
        self.paddle.move()
        self.ball.reset_position()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.state = "game"
            self.ball.set_speed()

    def game_state(self):
        self.paddle.move()
        self.ball.move()
        if self.ball.is_out():
            self.state = "init"

    def game_loop(self):
        while True:
            # Events: keyboard input
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            #move the paddle (update the position of the paddle)
            if self.state == "init": 
                self.init_state()
            elif self.state == "game":
                self.game_state()
            
            
            # Rendering: first clear with background and then draw each object
            # Blit everything to the screen (make background)
            self.screen.blit(self.background, (0, 0))

            #draw ball, paddle, and blocks on the screen
            self.wall.draw(self.screen)
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)