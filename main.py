import pygame
from player import Player
from constants import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	#Create groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	#Add all instances of the player class to both groups
	Player.containers = (updatable, drawable)

	#Spawn player in middle of screeen
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

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

		#Get move inputs
		for player in updatable:
			player.update(dt)

		#Draw player on screen
		for player in drawable:
			player.draw(screen)

		#Limit FPS to 60 and calculate fps
		dt = clock.tick(60) / 1000

		#Flip to next frame
		pygame.display.flip()

#Help ensure we run straight from a main command and isn't called
if __name__ == "__main__":
    main()
