import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x,y,radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "pink", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
	
	def split(self):
		self.kill()
		if self.radius == ASTEROID_MIN_RADIUS:
			return
		else:
			angle = random.uniform(20,50)
			vector1 = pygame.math.Vector2.rotate(self.velocity, angle)
			vector2 = pygame.math.Vector2.rotate(self.velocity, -angle)
			radius1 = self.radius - ASTEROID_MIN_RADIUS
			radius2 = self.radius - ASTEROID_MIN_RADIUS
			asteroid1 = Asteroid(self.position.x, self.position.y, radius1)
			asteroid1.velocity = vector1 * 1.2
			asteroid2 = Asteroid(self.position.x, self.position.y, radius2)
			asteroid2.velocity = vector2 * 1.2