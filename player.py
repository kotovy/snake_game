import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BLOCK_SIZE = 25
SNAKE_SPEED = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

pygame.mixer.init()
level_up_sound = pygame.mixer.Sound("res/level_upgrade.mp3")


def message(msg, color, y_displace=0, size="large"):
    font_styles = {
        "small": pygame.font.SysFont(None, 25),
        "medium": pygame.font.SysFont(None, 50),
        "large": pygame.font.SysFont(None, 80)
    }
    font_style = font_styles[size]
    rendered_msg = font_style.render(msg, True, color)
    text_width = rendered_msg.get_width()
    text_height = rendered_msg.get_height()
    screen.blit(rendered_msg, [SCREEN_WIDTH / 2 - text_width / 2, SCREEN_HEIGHT / 2 - text_height / 2 + y_displace])


def game_loop():
    game_over = False
    game_exit = False

    score = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    dx = 0
    dy = 0

    snake_segments = []
    snake_length = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_exit:
        while game_over:
            screen.fill(BLACK)
            message("Game over!", RED, y_displace=-50, size="large")
            message("Score: " + str(score), WHITE, y_displace=0, size="medium")
            message("Press C to continue or Q to exit.", WHITE, y_displace=50, size="small")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        score = 0
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != BLOCK_SIZE:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx != -BLOCK_SIZE:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy != BLOCK_SIZE:
                    dx = 0
                    dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy != -BLOCK_SIZE:
                    dx = 0
                    dy = BLOCK_SIZE

        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_over = True

        x += dx
        y += dy

        screen.fill(BLACK)

        pygame.draw.rect(screen, GREEN, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_segments.append(snake_head)

        if len(snake_segments) > snake_length:
            del snake_segments[0]

        for segment in snake_segments[:-1]:
            if segment == snake_head:
                game_over = True

        for segment in snake_segments:
            pygame.draw.rect(screen, WHITE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1
            score += 1
            level_up_sound.play()

        clock.tick(SNAKE_SPEED)


game_loop()
