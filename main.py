import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BACKGROUND_COLOR, MAX_FPS, FONT_SIZE
from logger import log_state
from player import Player
from logger import log_event
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, FONT_SIZE)

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player setup
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Asteroid setup
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Shots
    Shot.containers = (updatable, drawable, shots)

    score = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOR)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")

                    # Score: smaller asteroids are worth more.
                    # Uses integer division to keep values stable.
                    radius_factor = max(1, int(asteroid.radius // 10))
                    score += max(10, 100 // radius_factor)

                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        asteroids.add(new_asteroids)
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)

        score_surface = font.render(f"Score: {score}", True, "red")
        screen.blit(score_surface, (10, 10))

        pygame.display.flip()
        
        dt = clock.tick(MAX_FPS) / 1000 # convert from milliseconds to seconds


if __name__ == "__main__":
    main()
