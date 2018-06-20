import sys
import pygame
from bullet import Bullet
from asteroid import Asteroid


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""Respond to keypress"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
		
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	"""Responds to key releases"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	
def check_events(ai_settings, screen, ship, bullets):
	"""Respond to keypresses and mouse events."""
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, 
			bullets)
			
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
def update_bullets(bullets):
	###Update the position of bullets to get rid of old bullets."""
	bullets.update()
		
	# Get rid of old bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
def update_screen(ai_settings, screen, ship, asteroids, bullets):
	"""Update images on screen and flip to new screen"""
	#redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
			bullet.draw_bullet()
	ship.blitme()
	asteroids.draw(screen)
	
	#watch the most recently drawn screen visible.
	pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
	# Create a new bullet and add it to the bullet group.
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
		
def get_number_asteroids_x(ai_settings, asteroid_width):
	"""Determine the number of asteroids that fit in a row"""
	available_space_x = ai_settings.screen_width - 2 * asteroid_width
	number_asteroids_x = int(available_space_x / (2 * asteroid_width))
	return number_asteroids_x

def get_number_rows(ai_settings, ship_height, asteroid_height)
	"""Determine the number of rows of aliens that fit on the screen."""
	available_space_y = (ai_settings.screen_height -
							(3 * asteroid_height) - ship_height)
	number_rows = int(available_space_y / (2 * asteroid_height))
	return number_rows

def create_asteroid(ai_settings, screen, asteroids, asteroid_number, row_number):
	"""Create a single aseroid and put it in a row"""
	# Create an asteroid and place it in the row
	asteroid = Asteroid(ai_settings, screen)
	asteroid.width = asteroid.rect.width
	asteroid.height = asteroid.rect.height
	asteroid.x = asteroid_width + 2 * asteroid_width * asteroid_number
	asteroid.rect.x = asteroid.x
	asteroid.rect.y - asteroid.rect.height + 2 * asteroid.rect.height * row_number
	asteroids.add(asteroid)

def create_asteroids(ai_settings, screen, asteroids):
	"""Create a full array of asteroids"""
	# Create an asteroid and find the number of asteroids in a row
	# Spacing between each asteroid is equal to one asteroid width
	asteroid = Asteroid(ai_settings, screen)
	number_asteroids_x = get_number_asteroids_x(ai_settings, asteroid.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height), 
					asteroid.rect.height)
	
	# Create the fleet of asteroids
	for row_number in range(number_rows):
		for asteroid_number in range(number_asteroids_x):
			create_asteroid(ai_settings, screen, asteroids, asteroid_number, row_number)
