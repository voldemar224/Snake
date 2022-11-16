import const
import pygame


class Block:

    def __init__(self, x, y, screen, width=const.BLOCK_WIDTH, color=const.WHITE):
        self.x = x
        self.y = y
        self.screen = screen
        self.width = width
        self.color = color

    def draw_block(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width - 1, self.width - 1), 0, 7)
