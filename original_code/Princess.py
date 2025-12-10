
import pygame

class Princess(pygame.sprite.Sprite):
    """
       A princess character in the game with a position and image.
     """
    def __init__(self, x, y):
        """Initialize the princess with a position and sprite image."""
        super().__init__()
        self.image = pygame.image.load("../image/princess.png")  # use your sprite
        self.rect = self.image.get_rect(topleft=(x, y))
