import pygame
from block import Wall, Block
from paddle import Paddle
from constant import *

class Ball:
    def __init__(self, paddle: Paddle, wall: Wall):
        self.radius = 10
        self.color = WHITE
        self.paddle = paddle
        self.wall = wall
        self.reset_position()
    
    def reset_position(self):
        self.x = self.paddle.x + (self.paddle.width/2)
        self.y = self.paddle.y - self.radius

    def set_speed(self):
        self.speed_x = 2
        self.speed_y = -10

    def handle_screen_collision(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0:
            self.speed_y = -self.speed_y
    
    def handle_paddle_collision(self):
        if self.y + self.radius >= self.paddle.y and self.x - self.radius >= self.paddle.x and (self.x + self.radius) <= (self.paddle.x + self.paddle.width):
            self.speed_y = -self.speed_y
            self.speed_x *= 1.05
            self.speed_y *= 1.05
            self.paddle.speed *= 1.05

    
    def check_block_collision(self, block: Block):
        #False if the ball is above the block
        if self.y + self.radius < block.y:
            return False
        #False if the ball is below the block
        if self.y - self.radius > block.y + block.height:
            return False
        #False if the ball is on the left of the block
        if self.x + self.radius < block.x:
            return False
        #False if the ball is on the right if the block
        if self.x - self.radius > block.x + block.width:
            return False
        
        return True

    def handle_wall_collision(self):
        for block in self.wall.block_lists:
            if self.check_block_collision(block):
                if self.x > block.x + block.width or self.x < block.x:
                    self.speed_x = -self.speed_x
                else:
                    self.speed_y = -self.speed_y
                self.wall.block_lists.remove(block)

    def is_out(self):
        if self.y - self.radius > SCREEN_HEIGHT:
            return True
        return False

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.handle_screen_collision()
        self.handle_paddle_collision()
        self.handle_wall_collision()
    
    def draw(self, screen):
        pygame.draw.circle( 
            surface=screen, color=self.color, center=(self.x, self.y), radius=self.radius)
    

