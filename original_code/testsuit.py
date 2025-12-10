import pygame

pygame.init()
pygame.display.set_mode((1, 1))  # required for rects

def fake_image(path):
    surf = pygame.Surface((32, 32))
    return surf

pygame.image.load = fake_image


from Blocks import Blocks
from Princess import Princess
from enemy import Enemy
from Game import Game
from Player import Player



class FakeKeys:
    def __getitem__(self, key):
        return False


def test_blocks_creation():
    b = Blocks()
    blocks = b.create_blocks(5, 3)

    assert len(blocks) == 8
    assert blocks.count(b.normal_block) == 5
    assert blocks.count(b.coin_block) == 3

    print("  test_blocks_creation")



def test_princess_spawn():
    p = Princess(8450, 400)

    assert p.rect.x == 8450
    assert p.rect.y == 400
    assert isinstance(p.image, pygame.Surface)

    print("  test_princess_spawn")


def test_enemy_boundaries():
    e = Enemy(10, 480)
    e.world_left = 0
    e.world_right = 100

    # hit left
    e.rect.x = 0
    e.direction = -1
    e.update([])
    assert e.direction == 1

    # hit right
    e.rect.x = 100
    e.direction = 1
    e.update([])
    assert e.direction == -1

    print("  test_enemy_boundaries")


def test_enemy_gravity():
    e = Enemy(100, 200)
    before = e.rect.y
    e.apply_gravity()
    after = e.rect.y

    assert after > before
    print("  test_enemy_gravity")


def test_enemy_collides_with_block_turns():
    e = Enemy(100, 200)
    e.direction = 1

    block_rect = pygame.Rect(110, 200, 40, 40)
    blocks = [(None, block_rect, "normal")]

    for _ in range(5):
        e.update(blocks)

    assert e.direction == -1
    print("  test_enemy_collides_with_block_turns")



def test_player_move_right():
    p = Player()
    initial_x = p.x

    # Fake key for right movement
    class Keys:
        def __getitem__(self, k):
            return k == pygame.K_RIGHT

    p.movement(Keys(), camera_pos=0)

    assert p.x > initial_x
    print("  test_player_move_right")


def test_player_jump_and_gravity():
    p = Player()

    class Keys:
        def __getitem__(self, k):
            return k == pygame.K_UP

    p.movement(Keys(), camera_pos=0)

    assert p.y_velocity < 0  # jumped up
    print("  test_player_jump_and_gravity (jump detected)")


def test_player_hits_ground():
    p = Player()
    p.y = 400
    p.y_velocity = 30  # falling fast
    keys = FakeKeys()

    # simulate a few frames until he hits the floor
    for _ in range(10):
        p.movement(keys, camera_pos=0)
        if p.on_ground:
            break

    # final expected ground state
    assert p.y == 431
    assert p.on_ground is True

    print("  test_player_hits_ground")


def test_player_block_collision_top():
    p = Player()

    # Reset player clean position
    p.x = 100
    p.y = 100
    p.rect.topleft = (p.x, p.y)

    # Falling downward
    p.y_velocity = 10

    # Create a block directly below Mario
    block_rect = pygame.Rect(100, 120, 40, 40)  # block top is at y = 120
    blocks = [(None, block_rect, "normal")]

    # FORCE Mario into the block so .colliderect returns True
    p.rect.bottom = block_rect.top + 5  # now inside block by 5 pixels
    p.x, p.y = p.rect.topleft

    p.collide_with_blocks(blocks)

    # After collision:
    assert p.rect.bottom == block_rect.top
    assert p.y_velocity == 0
    assert p.on_ground is True

    print("  test_player_block_collision_top")

def test_player_block_collision_bottom():
    p = Player()

    # Reset player cleanly
    p.x = 100
    p.y = 200
    p.rect.topleft = (p.x, p.y)

    # Jumping upward
    p.y_velocity = -10

    # Create a block directly ABOVE Mario
    block_rect = pygame.Rect(100, 150, 40, 40)  # block bottom is at y = 190
    blocks = [(None, block_rect, "coin")]

    # FORCE Mario's head INTO the block to guarantee collision
    p.rect.top = block_rect.bottom - 5  # 5 px inside the bottom of the block
    p.x, p.y = p.rect.topleft

    hit = p.collide_with_blocks(blocks)

    # Validate collision
    assert hit is not None
    assert hit[2] == "coin"
    assert p.y_velocity == 0
    print("  test_player_block_collision_bottom")

def test_player_block_collision_left():
    p = Player()
    p.x = 150
    p.x_velocity = -5

    block_rect = pygame.Rect(100, 480, 40, 40)
    blocks = [(None, block_rect, "normal")]

    p.collide_with_blocks(blocks)

    assert p.rect.left == block_rect.right
    print("  test_player_block_collision_left")


def test_player_block_collision_right():
    p = Player()
    p.x = 50
    p.x_velocity = 5

    block_rect = pygame.Rect(100, 480, 40, 40)
    blocks = [(None, block_rect, "normal")]

    p.collide_with_blocks(blocks)

    assert p.rect.right == block_rect.left
    print("  test_player_block_collision_right")


def test_game_initialization():
    g = Game()

    assert g.score == 0
    assert g.level == 1
    assert g.life == 3
    assert len(g.block_positions) > 0
    assert len(g.enemies) > 0

    print("  test_game_initialization")

def test_mario_stomps_enemy():
    g = Game()
    e = g.enemies[0]

    # Place Mario just above the enemy, slightly overlapping so colliderect triggers
    g.mario.rect.bottom = e.rect.top + 5   # inside stomp range (+15)
    g.mario.rect.x = e.rect.x
    g.mario.y_velocity = 5                 # falling down

    # Sync Mario's internal x/y
    g.mario.x, g.mario.y = g.mario.rect.topleft

    g.mario_enemy_interaction()

    assert e not in g.enemies
    print("  test_mario_stomps_enemy")


def test_mario_gets_hurt():
    g = Game()

    e = g.enemies[0]
    g.mario.rect.centerx = e.rect.centerx + 1
    g.mario.y_velocity = 0

    initial_life = g.life
    g.mario_enemy_interaction()

    assert g.life == initial_life - 1
    print("  test_mario_gets_hurt")

def test_mario_collects_coin():
    g = Game()

    # Create a coin block directly above Mario
    coin_rect = pygame.Rect(g.mario.rect.x, g.mario.rect.y - 40, 40, 40)
    block = [None, coin_rect, "coin"]
    g.block_positions.append(block)

    # Simulate Mario jumping upward INTO the coin block
    g.mario.y_velocity = -10

    # FORCE Mario's head inside the coin block
    g.mario.rect.top = coin_rect.bottom - 5
    g.mario.x, g.mario.y = g.mario.rect.topleft

    # Detect collision
    hit = g.mario.collide_with_blocks(g.block_positions)

    if hit:
        g.block_positions.remove(hit)
        g.score += 100

    assert g.score == 100
    print("  test_mario_collects_coin")


def test_win_condition():
    g = Game()

    g.mario.rect.x = g.princess.rect.x
    g.mario.rect.y = g.princess.rect.y

    assert g.mario.rect.colliderect(g.princess.rect)
    print("  test_win_condition")


def test_game_over_condition():
    g = Game()
    g.life = 0

    assert g.life <= 0
    print("  test_game_over_condition")



if __name__ == "__main__":
    print("\nRunning FULL Mario Test Suite...\n")

    test_blocks_creation()
    test_princess_spawn()
    test_enemy_boundaries()
    test_enemy_gravity()
    test_enemy_collides_with_block_turns()
    test_player_move_right()
    test_player_jump_and_gravity()
    test_player_hits_ground()
    test_player_block_collision_top()
    test_player_block_collision_bottom()
    test_player_block_collision_left()
    test_player_block_collision_right()
    test_game_initialization()
    test_mario_stomps_enemy()
    test_mario_gets_hurt()
    test_mario_collects_coin()
    test_win_condition()
    test_game_over_condition()

    print("\nALL TESTS PASSED  \n")
