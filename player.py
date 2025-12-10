import pygame

RED = (255, 0, 0)
HEIGHT = 500

class Player(pygame.sprite.Sprite):
    """
     A simple player that can move left/right, jump, and collide with platforms.
    """

    def __init__(self):
            super().__init__()
            """Set up the player's sprite, position, and movement settings."""
            ...
            # Create a visual rectangle for the player
            self.surf = pygame.Surface((40, 50))
            self.surf.fill(RED)
            self.rect = self.surf.get_rect(midbottom=(100, HEIGHT - 50))

            self.vel_y = 0         # Vertical speed (used for jumping and gravity)
            self.speed = 5         # Horizontal speed (left/right movement)
            self.jump_power = -15  # Jump strength (negative moves up in Pygame)
            self.on_ground = False # Tracks if the player is standing on a platform

    def update(self, keys, platforms):
            """
                Update player movement, apply gravity, handle jumping,
                and check collisions with platforms.
                """


            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

            # Gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10

            self.rect.y += self.vel_y

            # Collision detection
            self.on_ground = False
            for p in platforms:
                if self.rect.colliderect(p.rect):
                    if self.vel_y > 0:
                        self.rect.bottom = p.rect.top
                        self.vel_y = 0
                        self.on_ground = True

            # Jump
            if keys[pygame.K_SPACE] and self.on_ground:
                self.vel_y = self.jump_power