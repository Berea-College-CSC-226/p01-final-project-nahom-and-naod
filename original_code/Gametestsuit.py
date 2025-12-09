from Game import Game

g = Game()



# Window size
assert g.size == (800, 600), "Game window size is incorrect."

# Mario exists
assert g.mario is not None, "Mario was not created."

# Blocks exist
assert len(g.block_positions) > 0, "Blocks did not generate."

# Enemies exist
assert len(g.enemies) > 0, "Enemies did not spawn."

# Score starts at 0
assert g.score == 0, "Score should start at 0."

# Lives start at 3
assert g.life == 3, "Lives should start at 3."


for e in g.enemies:
    assert e.rect.y == 480, "Enemy should spawn on ground (y = 480)."
    assert 0 <= e.rect.x <= 5000, "Enemy x-position is outside world bounds."



assert g.mario.x == 100, "Mario should start at x=100."
assert g.mario.y == 480, "Mario should start at ground level."


print("All Game tests passed successfully!")
