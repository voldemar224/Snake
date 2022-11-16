import pygame
import sys
import const

from apple import Apple
from snake import Snake

screen = pygame.display.set_mode((const.FIELD_WIDTH, const.FIELD_HEIGHT))

snake = Snake()
snake.create()
snake.draw_snake(screen)

apple = Apple()
apple.create_apple(snake)
apple.draw_block(screen)

pygame.display.update()

turn_timer = 0

game_timer = 0

while True:
    if not snake.game_over():
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                if not snake.turn_timer_is_on:
                    if i.key == pygame.K_LEFT:
                        snake.change_direction(const.K_LEFT)
                    elif i.key == pygame.K_RIGHT:
                        snake.change_direction(const.K_RIGHT)
                    elif i.key == pygame.K_UP:
                        snake.change_direction(const.K_UP)
                    elif i.key == pygame.K_DOWN:
                        snake.change_direction(const.K_DOWN)
        if snake.turn_timer_is_on:
            turn_timer += const.TURN_PAUSE_ADD
            if turn_timer >= const.TURN_PAUSE:
                snake.turn_timer_is_on = False
                turn_timer = 0

        if game_timer < const.MOVE_PAUSE:
            game_timer += const.MOVE_PAUSE_ADD
        else:
            game_timer = 0

            screen.fill(const.BLACK)

            snake.move()

            if apple.was_eaten(snake):
                snake.add()

                snake.draw_snake(screen)

                apple.create_apple(snake)
            else:
                apple.draw_block(screen)
                snake.draw_snake(screen)

        pygame.display.update()
