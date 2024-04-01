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
        paddle_left_edge_area = [self.paddle.x, self.paddle.x+(self.paddle.width/3)*1]
        #paddle_center_area = [(self.paddle.x+self.paddle.width/3)*1, self.paddle.x+(self.paddle.width/3)*2]
        paddle_right_edge_area = [(self.paddle.x+self.paddle.width/3)*2, self.paddle.x+self.paddle.width]

        if self.y + self.radius >= self.paddle.y and self.x - self.radius >= self.paddle.x and (self.x + self.radius) <= (self.paddle.x + self.paddle.width):
            if self.x >= paddle_left_edge_area[0] and self.x <= paddle_left_edge_area[1] -1:  
                self.speed_x = -(abs(self.speed_x) *1.5)
            elif self.x >= paddle_right_edge_area[0]+1 and self.x <= paddle_right_edge_area[1]:
                self.speed_x = abs(self.speed_x) *1.5
            else:
                pass

            self.speed_y = -self.speed_y
            self.speed_x *= 1.02
            self.speed_y *= 1.02
            self.paddle.speed *= 1.02
    
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
                block.hits -= 1
                if self.x > block.x + block.width or self.x < block.x:
                    self.speed_x = -self.speed_x
                else:
                    self.speed_y = -self.speed_y
                if block.hits == 0:
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
    

