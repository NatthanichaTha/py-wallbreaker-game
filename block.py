from constant import *
from utils import draw_rect_outline
from random import randint

class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hits = randint(1, 2)
    
    def draw(self, screen):
        color = PINK if self.hits == 1 else GRAY
        draw_rect_outline(screen, color, self.x, self.y, self.width, self.height)

class Wall:
    def __init__(self):
        #create wall of blocks
        self.blocks_per_line = 10
        lines = 8
        self.block_width = SCREEN_WIDTH/self.blocks_per_line
        self.block_height = 30

        self.block_lists = []
        x = 0
        y = 0

        for i in range(lines):
            for j in range(self.blocks_per_line+1):
                block = Block(x, y, self.block_width, self.block_height)
                self.block_lists.append(block)
                x += self.block_width
            x = 0
            y += self.block_height
    
    def add_row(self):
        #change the y position of all the existed blocks (y+=self.block_height)
        for block in self.block_lists:
            block.y += self.block_height
        #add new row of wall by insert blocks*(self.blocks_per_line) at the first row
            x = 0
            y = 0
        for i in range(self.blocks_per_line):
            block = Block(x, y, self.block_width, self.block_height)
            self.block_lists.insert(i, block)
            x += self.block_width        
        
    def draw(self, screen):
        for block in self.block_lists:
            block.draw(screen)

    



