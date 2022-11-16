from block import Block
import random
import const


class Apple(Block):
    def __init__(self, x=0, y=0, width=const.BLOCK_WIDTH, state=const.STATE, color=const.RED):
        Block.__init__(self, x, y, width)
        self.color = color
        self.state = state

    def create_apple(self, snake):
        self.state = True
        while self.state:
            self.state = False
            self.x = random.randint(1, const.FIELD_WIDTH / const.BLOCK_WIDTH) * const.BLOCK_WIDTH - const.BLOCK_WIDTH
            self.y = random.randint(1, const.FIELD_HEIGHT / const.BLOCK_WIDTH) * const.BLOCK_WIDTH - const.BLOCK_WIDTH
            for block in snake.blocks_list:
                if block.x == self.x and block.y == self.y:
                    self.state = True
                    break

    def was_eaten(self, snake):
        return snake.blocks_list[0].x == self.x and snake.blocks_list[0].y == self.y
