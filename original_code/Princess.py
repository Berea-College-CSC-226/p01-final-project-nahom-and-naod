
import pygame

class Princess(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../image/princess.png")  # use your sprite
        self.rect = self.image.get_rect(topleft=(x, y))
