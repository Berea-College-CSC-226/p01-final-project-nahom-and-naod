import turtle

class Enemy:
    """
    The Enemy class represents a simple moving enemy in the platformer.
    Enemies will move left and right and can interact with the player.
    """

    def __init__(self, x, y):
        """
        Set the starting position of the enemy and create the turtle
        that will draw it on the screen.
        """
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("red")
        self.turtle.penup()

        self.x = x
        self.y = y
        self.speed = 2       # how fast it moves
        self.direction = 1   # 1 = right, -1 = left

        # place enemy at starting location
        self.turtle.goto(self.x, self.y)

    def update(self):
        """
        Move the enemy left or right depending on its direction.
        This can later include edge detection or turning around.
        """
        self.x += self.speed * self.direction
        self.turtle.goto(self.x, self.y)

    def turn_around(self):
        """
        Reverse the direction of the enemy's movement.
        """
        self.direction *= -1

    def check_player_hit(self, player):
        """
        Check if the enemy touches the player. This will be filled in
        later when collision detection is added.
        """
        pass
