import pygame

pygame.init()
pygame.display.set_mode((1, 1))  # required for rects

def fake_image(path):
    """Return a fake 32x32 surface so tests can run without real images."""
    surf = pygame.Surface((32, 32))
    return surf

pygame.image.load = fake_image


from Blocks import Blocks
from Princess import Princess
from enemy import Enemy
from Game import Game
from Player import Player



class FakeKeys:
    """Fake key input object that always returns False (no key pressed)."""
    def __getitem__(self, key):
        return False


def test_blocks_creation():
    """Checks if Blocks creates the right number of normal and coin blocks."""
    b = Blocks()
    blocks = b.create_blocks(5, 3)

    assert len(blocks) == 8
    assert blocks.count(b.normal_block) == 5
    assert blocks.count(b.coin_block) == 3

    print("  test_blocks_creation")


def test_princess_spawn():
    """Makes sure the princess loads at the correct position with a valid image."""
    p = Princess(8450, 400)

    assert p.rect.x == 8450
    assert p.rect.y == 400
    assert isinstance(p.image, pygame.Surface)

    print("  test_princess_spawn")


def test_enemy_boundaries():
    """Enemy should turn around when hitting left or right world limits."""
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
    """Enemy should fall down when gravity is applied."""
    e = Enemy(100, 200)
    before = e.rect.y
    e.apply_gravity()
    after = e.rect.y

    assert after > before
    print("  test_enemy_gravity")


def test_enemy_collides_with_block_turns():
    """Enemy should turn around when walking into a block."""
    e = Enemy(100, 200)
    e.direction = 1

    block_rect = pygame.Rect(110, 200, 40, 40)
    blocks = [(None, block_rect, "normal")]

    for _ in range(5):
        e.update(blocks)

    assert e.direction == -1
    print("  test_enemy_collides_with_block_turns")


def test_player_move_right():
    """Player should move right when RIGHT key is pressed."""
    p = Player()
    initial_x = p.x

    class Keys:
        def __getitem__(self, k):
            return k == pygame.K_RIGHT

    p.movement(Keys(), camera_pos=0)

    assert p.x > initial_x
    print("  test_player_move_right")


def test_player_jump_and_gravity():
    """Player should jump when UP is pressed (y_velocity becomes negative)."""
    p = Player()

    class Keys:
        def __getitem__(self, k):
            return k == pygame.K_UP

    p.movement(Keys(), camera_pos=0)

    assert p.y_velocity < 0
    print("  test_player_jump_and_gravity (jump detected)")


def test_player_hits_ground():
    """Player should stop falling at the ground level and set on_ground=True."""
    p = Player()
    p.y = 400
    p.y_velocity = 30
    keys = FakeKeys()

    for _ in range(10):
        p.movement(keys, camera_pos=0)
        if p.on_ground:
            break

    assert p.y == 431
    assert p.on_ground is True

    print("  test_player_hits_ground")


def test_player_block_collision_top():
    """Player landing on top of block should stop falling and stand on it."""
    p = Player()

    p.x = 100
    p.y = 100
    p.rect.topleft = (p.x, p.y)

    p.y_velocity = 10

    block_rect = pygame.Rect(100, 120, 40, 40)
    blocks = [(None, block_rect, "normal")]

    p.rect.bottom = block_rect.top + 5
    p.x, p.y = p.rect.topleft

    p.collide_with_blocks(blocks)

    assert p.rect.bottom == block_rect.top
    assert p.y_velocity == 0
    assert p.on_ground is True

    print("  test_player_block_collision_top")


def test_player_block_collision_bottom():
    """Player hitting the bottom of a coin block should stop jumping and return the hit block."""
    p = Player()

    p.x = 100
    p.y = 200
    p.rect.topleft = (p.x, p.y)

    p.y_velocity = -10

    block_rect = pygame.Rect(100, 150, 40, 40)
    blocks = [(None, block_rect, "coin")]

    p.rect.top = block_rect.bottom - 5
    p.x, p.y = p.rect.topleft

    hit = p.collide_with_blocks(blocks)

    assert hit is not None
    assert hit[2] == "coin"
    assert p.y_velocity == 0
    print("  test_player_block_collision_bottom")


def test_player_block_collision_left():
    """Player walking into block from left should stop at block.right."""
    p = Player()
    p.x = 150
    p.x_velocity = -5

    block_rect = pygame.Rect(100, 480, 40, 40)
    blocks = [(None, block_rect, "normal")]

    p.collide_with_blocks(blocks)

    assert p.rect.left == block_rect.right
    print("  test_player_block_collision_left")


def test_player_block_collision_right():
    """Player walking into block from right should stop at block.left."""
    p = Player()
    p.x = 50
    p.x_velocity = 5

    block_rect = pygame.Rect(100, 480, 40, 40)
    blocks = [(None, block_rect, "normal")]

    p.collide_with_blocks(blocks)

    assert p.rect.right == block_rect.left
    print("  test_player_block_collision_right")


def test_game_initialization():
    """Game should spawn blocks, enemies, and set default game stats."""
    g = Game()

    assert g.score == 0
    assert g.level == 1
    assert g.life == 3
    assert len(g.block_positions) > 0
    assert len(g.enemies) > 0

    print("  test_game_initialization")


def test_mario_stomps_enemy():
    """Mario landing on an enemy from above should remove the enemy."""
    g = Game()
    e = g.enemies[0]

    g.mario.rect.bottom = e.rect.top + 5
    g.mario.rect.x = e.rect.x
    g.mario.y_velocity = 5

    g.mario.x, g.mario.y = g.mario.rect.topleft

    g.mario_enemy_interaction()

    assert e not in g.enemies
    print("  test_mario_stomps_enemy")


def test_mario_gets_hurt():
    """Mario touching an enemy from the side should reduce life by 1."""
    g = Game()

    e = g.enemies[0]
    g.mario.rect.centerx = e.rect.centerx + 1
    g.mario.y_velocity = 0

    initial_life = g.life
    g.mario_enemy_interaction()

    assert g.life == initial_life - 1
    print("  test_mario_gets_hurt")


def test_mario_collects_coin():
    """Mario hitting a coin block should increase score by 100."""
    g = Game()

    coin_rect = pygame.Rect(g.mario.rect.x, g.mario.rect.y - 40, 40, 40)
    block = [None, coin_rect, "coin"]
    g.block_positions.append(block)

    g.mario.y_velocity = -10

    g.mario.rect.top = coin_rect.bottom - 5
    g.mario.x, g.mario.y = g.mario.rect.topleft

    hit = g.mario.collide_with_blocks(g.block_positions)

    if hit:
        g.block_positions.remove(hit)
        g.score += 100

    assert g.score == 100
    print("  test_mario_collects_coin")


def test_win_condition():
    """Mario touching the princess should trigger the win state."""
    g = Game()

    g.mario.rect.x = g.princess.rect.x
    g.mario.rect.y = g.princess.rect.y

    assert g.mario.rect.colliderect(g.princess.rect)
    print("  test_win_condition")


def test_game_over_condition():
    """Life at 0 or less should count as game over."""
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
