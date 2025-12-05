from circleshape import CircleShape
import pygame
from constants import ASTEROID_COLOR, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, ASTEROID_COLOR, (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)