import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 100
        self.y = 480

        self.character = pygame.image.load("../image/mario_4.png")
        self.rect = self.character.get_rect(topleft=(self.x, self.y))

        self.speed = 10
        self.x_velocity = 0

        self.y_velocity = 0
        self.gravity = 1
        self.jump_power = 20

        self.on_ground = True

    def movement(self, key, camera_pos):


        self.x_velocity = 0
        if key[pygame.K_RIGHT] and camera_pos < 5000:
            self.x_velocity = self.speed
        if key[pygame.K_LEFT] and camera_pos > 0:
            self.x_velocity = -self.speed

        self.x += self.x_velocity


        if key[pygame.K_UP] and self.on_ground:
            self.y_velocity = -self.jump_power
            self.on_ground = False


        self.y_velocity += self.gravity
        self.y += self.y_velocity


        if self.y >= 480:
            self.y = 480
            self.y_velocity = 0
            self.on_ground = True

        self.rect.topleft = (self.x, self.y)

    def collide_with_blocks(self, blocks):
        for block_img, rect in blocks:

            if self.rect.colliderect(rect):


                if self.y_velocity > 0 and self.rect.bottom > rect.top:
                    self.rect.bottom = rect.top
                    self.y_velocity = 0
                    self.on_ground = True


                elif self.y_velocity < 0 and self.rect.top < rect.bottom:
                    self.rect.top = rect.bottom
                    self.y_velocity = 0


                elif self.x_velocity > 0:
                    self.rect.right = rect.left

                elif self.x_velocity < 0:
                    self.rect.left = rect.right

        self.x, self.y = self.rect.topleft
