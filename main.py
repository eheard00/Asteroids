import sys
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	#Create groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	#Add all instances of the player class to both groups
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)

	#Spawn player in middle of screeen
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	#Create asteroid field
	asteroidfield = AsteroidField()

	#Set screen size
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	#Enter game loop
	while True:
		#Allows the x button to exit game.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		#Fills screen
		screen.fill("black")

		#Update sprites
		for sprite in updatable:
			sprite.update(dt)
			if isinstance(sprite, Player):
				sprite.PLAYER_SHOOT_COOLDOWN -= dt
			#Check if player sprite touches asteroids
			if isinstance(sprite, Asteroid):
				if sprite.collision(player) == True:
					print("Game Over!")
					sys.exit()
				#Check if the asteroid is touching a bullet
				for shot in updatable:
					if isinstance(shot, Shot):
						if shot.collision(sprite) == True:
							sprite.kill()
							shot.kill()
			

		#Draw objects on screen
		for sprite in drawable:
			sprite.draw(screen)

		#Limit FPS to 60 and calculate fps
		dt = clock.tick(60) / 1000

		#Flip to next frame
		pygame.display.flip()

#Help ensure we run straight from a main command and isn't called
if __name__ == "__main__":
    main()