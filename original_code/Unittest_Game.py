import unittest
from game import Game

class TestGame(unittest.TestCase):
    """
    Tests for the Game class. These tests make sure that the
    Game class initializes correctly and that its main methods
    work without throwing errors.
    """

    def setUp(self):
        """Create a Game object before each test."""
        self.game = Game()

    def test_initial_attributes(self):
        """Test that the Game object starts with the needed attributes."""
        self.assertIsNotNone(self.game.screen)
        self.assertIsNone(self.game.player)
        self.assertIsNone(self.game.level)
        self.assertIsInstance(self.game.enemies, list)
        self.assertTrue(self.game.running)

    def test_update_method_runs(self):
        """Test that update() can run without errors."""
        try:
            self.game.update()
        except Exception as e:
            self.fail(f"update() raised an exception: {e}")

    def test_draw_method_runs(self):
        """Test that draw() can run without errors."""
        try:
            self.game.draw()
        except Exception as e:
            self.fail(f"draw() raised an exception: {e}")

    def test_run_stops_when_running_is_false(self):
        """
        Test that the game loop will stop if running is set to False.
        We do NOT run the full loop because it depends on turtle graphics.
        """
        self.game.running = False
        try:
            # run one iteration manually for testing
            self.game.update()
            self.game.draw()
        except Exception as e:
            self.fail(f"Game loop logic failed when running was False: {e}")


if __name__ == "__main__":
    unittest.main()
