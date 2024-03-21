from constant import *
from utils import draw_rect_outline

class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = PINK
    
    def draw(self, screen):
        draw_rect_outline(screen, self.color, self.x, self.y, self.width, self.height)

class Wall:
    def __init__(self):
        #create wall of blocks
        blocks_per_line = 10
        lines = 8
        block_width = SCREEN_WIDTH/blocks_per_line
        block_height = 30

        self.block_list = []
        x = 0
        y = 0

        for i in range(lines):
            for j in range(blocks_per_line+1):
                block = Block(x, y, block_width, block_height)
                self.block_list.append(block)
                x += block_width
            x = 0
            y += block_height
        
        
    def draw(self, screen):
        for block in self.block_list:
            block.draw(screen)

            



