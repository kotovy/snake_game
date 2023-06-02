import pygame
from player import game_loop
from eat import food_x, food_y, BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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


game_loop()
