import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("../image/goombas.png")
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = 2
        self.direction = -1

        self.y_velocity = 0
        self.gravity = 1
        self.on_ground = False

        self.world_left = 0
        self.world_right = 5000

    def apply_gravity(self):
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity

    def move(self):
        self.rect.x += self.direction * self.speed

    def update(self, blocks):


        self.move()
        self.apply_gravity()

        if self.rect.x <= self.world_left:
            self.rect.x = self.world_left
            self.direction = 1

        if self.rect.x >= self.world_right:
            self.rect.x = self.world_right
            self.direction = -1


        for block_img, rect, block_type in blocks:
            if self.rect.colliderect(rect):

                if self.direction > 0 and self.rect.right > rect.left:
                    self.rect.right = rect.left
                    self.direction = -1

                elif self.direction < 0 and self.rect.left < rect.right:
                    self.rect.left = rect.right
                    self.direction = 1

        if self.rect.bottom >= 480:
            self.rect.bottom = 540
            self.y_velocity = 0
            self.on_ground = True
