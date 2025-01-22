import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
	def __init__(self,x,y):
		super().__init__(x,y,PLAYER_RADIUS)
		self.rotation = 0
		self.PLAYER_SHOOT_COOLDOWN = 0.0

# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	#Draws player onto screen
	def draw(self, screen):
		pygame.draw.polygon(screen, "purple", self.triangle(), 2)

	#Rotate player method
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	#Move player
	def move(self, dt):
		forward = pygame.Vector2(0,1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	#Update player
	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(dt*-1)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(dt*-1)
		if keys[pygame.K_SPACE]:
			self.shoot()

	def shoot(self):
		if not self.PLAYER_SHOOT_COOLDOWN > 0.0:
			self.PLAYER_SHOOT_COOLDOWN = 0.3
			shot = Shot(self.position.x, self.position.y)
			shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED