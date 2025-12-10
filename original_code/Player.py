import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 100
        self.y = 480

        self.character = pygame.image.load("../image/mario_4.png")
        self.rect = self.character.get_rect(topleft=(self.x, self.y))

        self.speed = 12
        self.x_velocity = 0

        self.y_velocity = 0
        self.gravity = 1
        self.jump_power = 20

        self.on_ground = True

    def movement(self, key, camera_pos):

        self.x_velocity = 0

        if key[pygame.K_RIGHT] and camera_pos < 8350:
            self.x_velocity += self.speed

        if key[pygame.K_LEFT] and camera_pos > 0:
            self.x_velocity = -self.speed

        self.x += self.x_velocity

        if key[pygame.K_UP] and self.on_ground:
            self.y_velocity = -self.jump_power
            self.on_ground = False

        # gravity
        self.y_velocity += self.gravity
        self.y += self.y_velocity

        # floor
        if self.y >= 480:
            self.y = 480
            self.y_velocity = 0
            self.on_ground = True

        # sync rect
        self.rect.topleft = (self.x, self.y)

    def collide_with_blocks(self, blocks):

        hit_from_below = None

        for block in blocks:
            block_img, rect, block_type = block

            if self.rect.colliderect(rect):

                # landing on top of a block
                if self.y_velocity > 0 and self.rect.bottom > rect.top:
                    self.rect.bottom = rect.top
                    self.y_velocity = 0
                    self.on_ground = True

                # hitting block from below (jumping up into it)
                elif self.y_velocity < 0 and self.rect.top <= rect.bottom:
                    self.rect.top = rect.bottom
                    self.y_velocity = 0
                    hit_from_below = block   # return the exact block object

                # walking into block from the right
                elif self.x_velocity > 0:
                    self.rect.right = rect.left

                # walking into block from the left
                elif self.x_velocity < 0:
                    self.rect.left = rect.right

        # update x, y from rect
        self.x, self.y = self.rect.topleft

        return hit_from_below
