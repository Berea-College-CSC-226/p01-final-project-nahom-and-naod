import pygame
pygame.init()

from Player import Player

def test_player_initial_state():
    p = Player()
    assert p.x == 100
    assert p.y == 480
    assert p.speed > 0
    assert p.gravity > 0
    assert p.jump_power > 0
    assert p.on_ground is True

def test_player_jump_changes_velocity():
    p = Player()
    p.on_ground = True
    p.y_velocity = 0

    keys = {pygame.K_UP: True}   # simulate up arrow
    p.movement(keys, camera_pos=0)

    assert p.y_velocity < 0, "Jump should give Mario upward velocity."
    assert p.on_ground is False

def test_player_gravity_applies():
    p = Player()
    p.on_ground = False
    p.y_velocity = 0

    p.movement({}, 0)
    assert p.y_velocity > 0, "Gravity should increase downward velocity."

def test_player_ground_collision():
    p = Player()
    p.y = 470
    p.y_velocity = 20

    p.movement({}, 0)

    assert p.y == 480, "Mario should not fall below ground."
    assert p.on_ground is True

def test_player_horizontal_movement():
    p = Player()
    keys = {pygame.K_RIGHT: True}

    old_x = p.x
    p.movement(keys, camera_pos=0)
    assert p.x > old_x, "Mario should move right."


if __name__ == "__main__":
    test_player_initial_state()
    test_player_jump_changes_velocity()
    test_player_gravity_applies()
    test_player_ground_collision()
    test_player_horizontal_movement()

    print("ALL PLAYER TESTS PASSED ✔")