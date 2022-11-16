from block import Block
import const


class Snake:

    def __init__(self, blocks_list=None, x=const.START_X, y=const.START_Y, length=const.SNAKE_LENGTH,
                 block_width=const.BLOCK_WIDTH, speed_x=const.SPEED_X, speed_y=const.SPEED_Y,
                 field_width=const.FIELD_WIDTH, field_height=const.FIELD_HEIGHT, turn_timer_is_on=False):
        if blocks_list is None:
            blocks_list = []
        self.blocks_list = blocks_list
        self.x = x
        self.y = y
        self.length = length
        self.block_width = block_width
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.field_width = field_width
        self.field_height = field_height
        self.turn_timer_is_on = turn_timer_is_on

    def create(self):
        for i in range(0, self.length):
            self.blocks_list.append(Block(self.x - i * self.block_width, self.y, self.block_width))

    def change_direction(self, direction):
        if direction == const.K_LEFT:
            if self.speed_x == 0:
                self.turn_timer_is_on = True
                self.speed_x = -self.block_width
                self.speed_y = 0
        elif direction == const.K_RIGHT:
            if self.speed_x == 0:
                self.turn_timer_is_on = True
                self.speed_x = self.block_width
                self.speed_y = 0
        elif direction == const.K_UP:
            if self.speed_y == 0:
                self.turn_timer_is_on = True
                self.speed_x = 0
                self.speed_y = -self.block_width
        elif direction == const.K_DOWN:
            if self.speed_y == 0:
                self.turn_timer_is_on = True
                self.speed_x = 0
                self.speed_y = self.block_width

    def move(self):
        for i in range(self.length - 1, 0, -1):
            self.blocks_list[i].x = self.blocks_list[i - 1].x
            self.blocks_list[i].y = self.blocks_list[i - 1].y

        self.blocks_list[0].x = (self.blocks_list[0].x + self.speed_x) % self.field_width
        self.blocks_list[0].y = (self.blocks_list[0].y + self.speed_y) % self.field_height

    def add(self):
        self.blocks_list.append(Block(self.blocks_list[self.length - 1].x, self.blocks_list[self.length - 1].y,
                                      self.block_width))
        self.length += 1

    def game_over(self):
        for i in range(1, self.length):
            if self.blocks_list[0].x == self.blocks_list[i].x and self.blocks_list[0].y == self.blocks_list[i].y:
                return True
        return False

    def draw_snake(self, screen):
        for block in self.blocks_list:
            block.draw_block(screen)
