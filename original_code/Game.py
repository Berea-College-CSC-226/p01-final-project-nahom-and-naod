import turtle

class Game:
    """
    The Game class sets up the turtle screen and prepares the main
    parts of the platformer. Later, it will manage the player,
    enemies, and level as the game runs.
    """

    def __init__(self):
        """
        Create the turtle screen and set up the basic game values.
        This is where the player, level, and enemies will be created.
        """
        self.screen = turtle.Screen()
        self.screen.title("Platformer Game")
        self.screen.setup(width=800, height=600)

        # These will be filled in later
        self.player = None
        self.level = None
        self.enemies = []

        self.running = True

    def run(self):
        """
        Start the game loop. This loop keeps the game running until
        the user closes the screen. The update and draw functions
        will run every frame.
        """
        while self.running:
            self.update()
            self.draw()
            self.screen.update()

    def update(self):
        """
        Update the game state. This will later include movement,
        collisions, and enemy behavior.
        """
        pass

    def draw(self):
        """
        Draw everything on the screen. This will later handle drawing
        the player, enemies, and level.
        """
        pass
