import pygame

from settings import Settings
from ship import Ship
from asteroid import Asteroid
import game_functions as gf
from pygame.sprite import Group

def run_game():
	#Initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Make a ship, a group to store bullets, and asteroids
	ship = Ship(ai_settings, screen)
	bullets = Group()
	asteroids = Group()
	
	# Create a row of asteroids
	gf.create_asteroids(ai_settings, screen, ship, asteroids)
	
	#start the main loop for the game
	while True:
		
		#watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, asteroids, bullets)		
		
run_game()
