import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_COLOR, SHOT_RADIUS, SHOT_LIFETIME_SECONDS


class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = 0
        self.lifetime = SHOT_LIFETIME_SECONDS

    def draw(self, screen):
      return pygame.draw.circle(screen, SHOT_COLOR, (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)

    def update(self, dt):
      self.position += (self.velocity * dt)