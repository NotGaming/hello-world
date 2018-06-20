import pygame
from pygame.sprite import Sprite

class Asteroid(Sprite):
	"""A class to represent a single asteroid."""
	
	def __init__(self, ai_settings, screen):
		""" Initialize the asteroid and set its starting position """
		super(Asteroid, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		# Load the asteroid image and set its rect attribute
		self.image = pygame.image.load('images/asteroid.bmp')
		self.rect = self.image.get_rect()
		
		# Start each new asteroid near the top of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# Store the alien's exact position.
		self.x = float(self.rect.x)
	
	def blitme(self):
		"""Draw the asteroid at its current location."""
		self.screen.blit(self.image, self.rect)
