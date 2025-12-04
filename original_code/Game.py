import pygame


class Game:
    def __init__(self):
        """
            Game class for handling the game logic.
        """
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#0001FC')
        self.clock = pygame.time.Clock()
        self.score = 0
        self.mario = None

        self.floor = pygame.image.load("../image/floor2.jpg").convert_alpha()
        self.player = pygame.image.load("../image/mario_1.png").convert_alpha()

    def run(self):
        """
        Runs the game until the player loses or wins

        """
        while self.running:
            # Handle game ending first
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            font = pygame.font.SysFont("ComicSans", 20)
            txt = font.render('Mini Super Mario', True, "red")
            self.screen.blit(txt, (10, 10))
            self.screen.blit(self.floor,(0,550))
            self.screen.blit(self.floor, (400,550))
            self.screen.blit(self.player, (20,500))

            pygame.display.update()
            self.clock.tick(24)
def main():
    game = Game()
    game.run()
main()