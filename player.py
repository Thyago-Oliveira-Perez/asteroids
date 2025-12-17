import pygame
from constants import (
	PLAYER_RADIUS,
	LINE_WIDTH,
	PLAYER_SHOOT_COOLDOWN_SECONDS,
	PLAYER_SHOT_SPEED,
	PLAYER_SPEED,
	PLAYER_TURN_SPEED,
	PLAYER_COLOR,
	SCREEN_WIDTH,
	SCREEN_HEIGHT,
)
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_cooldown = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		points = self.triangle()
		return pygame.draw.polygon(screen, PLAYER_COLOR, points, LINE_WIDTH)
	
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]: # left
				self.rotate(-dt)
		if keys[pygame.K_d]: # right
				self.rotate(dt)
		if keys[pygame.K_w]: # forward
				self.move(dt)
		if keys[pygame.K_s]: # backward
				self.move(-dt)
		if keys[pygame.K_SPACE]: # shoot
				self.shoot()

		self.shoot_cooldown -= dt

		# Wrap around screen edges (Asteroids-style).
		# Uses radius padding so the ship doesn't vanish abruptly.
		pad = self.radius
		if self.position.x < -pad:
			self.position.x = SCREEN_WIDTH + pad
		elif self.position.x > SCREEN_WIDTH + pad:
			self.position.x = -pad

		if self.position.y < -pad:
			self.position.y = SCREEN_HEIGHT + pad
		elif self.position.y > SCREEN_HEIGHT + pad:
			self.position.y = -pad


	def shoot(self):
		if self.shoot_cooldown > 0:
			return None

		self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

		shot = Shot(self.position)
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		shot.velocity = forward * PLAYER_SHOT_SPEED