import random
from circleshape import CircleShape
import pygame
from constants import ASTEROID_COLOR, ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, ASTEROID_COLOR, (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        angle = random.uniform(20, 50)

        asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid2.velocity = self.velocity.rotate(-angle) * 1.2

        return [asteroid1, asteroid2]