import turtle

class Player:
    """
    The Player class represents the main character in the platformer.
    This class will store the player's position, movement, and
    basic values like health and score.
    """

    def __init__(self, x, y):
        """
        Set up the player's starting position and create the turtle
        that will draw the player on the screen.
        """
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.penup()

        self.x = x
        self.y = y
        self.vx = 0      # left/right movement
        self.vy = 0      # up/down movement (jumping)

        self.health = 3
        self.score = 0

        # move the turtle to the starting position
        self.turtle.goto(self.x, self.y)

    def move_left(self):
        """
        Move the player to the left by changing its x-position.
        """
        self.vx = -5

    def move_right(self):
        """
        Move the player to the right by changing its x-position.
        """
        self.vx = 5

    def jump(self):
        """
        Make the player move upward. This will later work together
        with gravity inside update_position().
        """
        self.vy = 10

    def update_position(self):
        """
        Update the player's position based on movement values.
        This will later include gravity and collision checks.
        """
        self.x += self.vx
        self.y += self.vy
        self.turtle.goto(self.x, self.y)

    def check_collision(self, blocks):
        """
        Check if the player touches any blocks. This will be filled in
        later when blocks are created.
        """
        pass
