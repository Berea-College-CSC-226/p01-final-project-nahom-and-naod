import math
import pygame
import random
from Player import Player
from Blocks import Blocks
from enemy import Enemy

class Game:

    def __init__(self):
        pygame.init()
        self.size = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#4067B0')
        self.is_running = True
        self.clock = pygame.time.Clock()

        self.camera_x = 0
        self.score = 0
        self.level = 1
        self.life = 3

        self.mario = Player()
        self.blocks = Blocks()

        # Blocks
        self.block_positions = []
        self.generate_blocks()

        # Enemies
        self.enemies = []
        self.spawn_enemies()

        # Flowers
        self.flower_positions = []
        self.generate_flowers()



    def generate_flowers(self):
        self.flowers_images = [
            pygame.image.load("../image/flower0.png"),
            pygame.image.load("../image/flower1.png"),
            pygame.image.load("../image/flower2.png"),
            pygame.image.load("../image/flower3.png")
        ]

        self.flower_positions = []
        x = 0
        y = 510  # straight line height

        for _ in range(50):  # number of flowers
            img = random.choice(self.flowers_images)
            x += random.randint(80, 200)  # random horizontal spacing
            self.flower_positions.append((img, x, y))



    def generate_blocks(self):
        self.block_positions = []

        block_width = 45
        num_groups = 10
        start_x = 300

        for _ in range(num_groups):
            rand_normal = random.randint(2, 4)
            rand_coins = random.randint(0, 1)
            group = self.blocks.create_blocks(rand_normal, rand_coins)

            random.shuffle(group)
            group_start_x = start_x + random.randint(200, 300)

            for i, block in enumerate(group):
                x = group_start_x + i * block_width
                y = 390
                rect = block.get_rect(topleft=(x, y))
                block_type = "coin" if block == self.blocks.coin_block else "normal"
                self.block_positions.append([block, rect, block_type])

            start_x = group_start_x + 600

    def spawn_enemies(self):
        self.enemies = []
        for i in range(10):  # number of enemies
            x = random.randint(400, 5000)
            y = 480
            enemy = Enemy(x, y)
            self.enemies.append(enemy)



    def mario_enemy_interaction(self):
        for enemy in self.enemies[:]:
            if self.mario.rect.colliderect(enemy.rect):


                if (
                        self.mario.y_velocity > 0 and
                        self.mario.rect.bottom <= enemy.rect.top + 15
                ):
                    self.score += 1*100 # add score
                    self.mario.y_velocity = -15  # bounce
                    self.enemies.remove(enemy)  # kill enemy

                else:
                    self.life -= 1
                    self.mario.x -= 25
                    self.mario.y -= 25
                    self.mario.rect.x = self.mario.x


    def load_sprite(self):
        self.camera_x = self.mario.x - 100

        # Ground tiles
        ground = pygame.image.load("../image/floor2.jpg")
        for i in range(30):
            ground_x = (452 * i - self.camera_x) - 100
            self.screen.blit(ground, (ground_x, 542))

        # Clouds
        cloud = pygame.image.load("../image/cloud_2.png")
        for i in range(1, 30):
            cloud_x = (400 * i * math.sqrt(i) - self.camera_x)
            self.screen.blit(cloud, (cloud_x, math.sin(1 / i) * 30 + 50))

        # Flowers
        for img, x, y in self.flower_positions:
            draw_x = x - self.camera_x
            self.screen.blit(img, (draw_x, y))

        # HUD
        font_primary = pygame.font.SysFont('../fonts/SuperMario256.ttf', 40)
        font_secondary = pygame.font.SysFont("../fonts/SuperMario256.ttf", 35)

        self.screen.blit(font_primary.render('SCORE', True, "white"), (20, 20))
        self.screen.blit(font_secondary.render(str(self.score), True, "white"), (50, 50))

        self.screen.blit(font_primary.render('LIVES', True, "white"), (700, 20))
        self.screen.blit(font_secondary.render(str(self.life), True, "white"), (730, 50))

        # Logo
        super_mario_logo = pygame.image.load("../image/SUPERMARIO_LOGO_BIG.png")
        SML_size = super_mario_logo.get_size()
        pygame.draw.rect(self.screen,"#FF746C",(30-self.camera_x, 90 ,SML_size[0]+20,SML_size[1]+20),0,20)
        self.screen.blit(super_mario_logo, (40 - self.camera_x, 100))

        for block, rect, block_type in self.block_positions:
            draw_x = rect.x - self.camera_x
            self.screen.blit(block, (draw_x, rect.y))

        for enemy in self.enemies:
            draw_x = enemy.rect.x - self.camera_x
            self.screen.blit(enemy.image, (draw_x, enemy.rect.y))

        # Mario
        self.screen.blit(self.mario.character, (100, self.mario.y))

        # Debug Mario hitbox # remove at the end
        pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            (self.mario.rect.x - self.camera_x, self.mario.rect.y, self.mario.rect.width, self.mario.rect.height),
            2
        )


    def game_over_screen(self):
        font = pygame.font.SysFont('../fonts/SuperMario256.ttf', 70)
        font_score = pygame.font.SysFont('../fonts/SuperMario256.ttf', 35)

        text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.size[0] // 2, self.size[1] // 2))

        text_score = font_score.render(f"SCORE {self.score}", True, (255, 255, 0))
        text_score_rect = text_score.get_rect()
        text_score_rect.centerx = text_rect.centerx
        text_score_rect.top = text_rect.bottom + 20

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.is_running = False

            self.screen.fill((0, 0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(text_score, text_score_rect)
            pygame.display.update()
            self.clock.tick(10)



    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.screen.fill('#4067B0')

            self.load_sprite()

            key = pygame.key.get_pressed()
            self.camera_x = self.mario.x - 100

            self.mario.movement(key, self.camera_x)
            hit_block = self.mario.collide_with_blocks(self.block_positions)

            if hit_block:
                img, rect, block_type = hit_block

                if block_type == "normal":
                    self.block_positions.remove(hit_block)

                elif block_type == "coin":
                    self.score += 100
                    self.block_positions.remove(hit_block)

            # Enemy updates
            for enemy in self.enemies:
                enemy.update(self.block_positions)
            self.mario_enemy_interaction()

            if self.life <= 0:
                self.game_over_screen()
                return

            pygame.display.update()
            self.clock.tick(24)


def main():
    super_mario = Game()
    super_mario.run()


if __name__ == "__main__":
    main()
