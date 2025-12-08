import pygame

class Blocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.normal_block = pygame.image.load("../image/Block_3.png")
        self.coin_block = pygame.image.load("../image/Prize_block_3.png")

    def create_blocks(self, num_blocks, num_coins):
        lst = []
        for i in range(num_blocks):
            lst.append(self.normal_block)
        for i in range(num_coins):
            lst.append(self.coin_block)
        return lst
