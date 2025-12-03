import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

MAX_FPS = 60
BACKGROUND_COLOR = "black"

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOR)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(MAX_FPS) / 1000 # convert from milliseconds to seconds


if __name__ == "__main__":
    main()
