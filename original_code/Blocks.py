import pygame

class Blocks(pygame.sprite.Sprite):
    """Loads block images and provides tools for creating block lists."""

    def __init__(self):
        """Load normal and coin block images into memory."""
        super().__init__()
        self.normal_block = pygame.image.load("../image/Block_3.png")
        self.coin_block = pygame.image.load("../image/Prize_block_3.png")

    def create_blocks(self, num_blocks, num_coins):
        """Return a list of normal and coin blocks based on given counts."""
        lst = []
        for _ in range(num_blocks):
            lst.append(self.normal_block)
        for _ in range(num_coins):
            lst.append(self.coin_block)
        return lst
