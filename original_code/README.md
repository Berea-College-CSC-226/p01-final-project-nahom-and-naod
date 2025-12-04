This folder is for holding your original assignments that you are using as a reference. 
Put the code in this folder, but DO NOT modify it directly! 


import pygame
from t11_NPC import NPC, Good_NPC, Bad_NPC
from t11_player import Player


class Game:
    def __init__(self):
        """
        Game class for handling the game logic.
        """
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#9CBEBA')
        self.clock = pygame.time.Clock()
        self.tuna = Player(self.size)
        self.tacocat = Good_NPC(self.size)
        self.whiskers = Bad_NPC(self.size)

        self.score = 1


    def run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:
            # Handle game ending first
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            font = pygame.font.SysFont("ComicSans", 36)
            txt = font.render(f'lives left {self.score}', True, "darkblue")
            self.screen.blit(txt, (50,50))
            # Handle user and game events next
            if pygame.sprite.spritecollide(self.tuna, [self.tacocat], False):
                # Prints the game ending text to the screen
                font = pygame.font.SysFont("ComicSans", 36)
                txt = font.render('You caught me! \n You gained a life', True, "darkblue")
                self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
                self.score += 1
                # import time
                # time.sleep(1)
                # return
            elif pygame.sprite.spritecollide(self.tuna, [self.whiskers], False):
                # Prints the game ending text to the screen
                font = pygame.font.SysFont("ComicSans", 36)
                txt = font.render('Oh no! Caught by Whiskers :( \n You lost a life', True, "darkblue")
                self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
                self.score -= 1

            else:
                # Keep playing!
                self.tuna.movement(pygame.key.get_pressed())
                self.tacocat.movement()
                self.whiskers.movement()
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.tuna.surf, self.tuna.rect)
                self.screen.blit(self.tacocat.surf, self.tacocat.rect)
                self.screen.blit(self.whiskers.surf, self.whiskers.rect)
            pygame.display.update()
            self.clock.tick(24)

        pygame.quit()


def main():
    """
    Starts the cat game.

    :return: None
    """
    game = Game()
    while True:
        print("Running")
        game.run()
        if not game.score or game.score == 2 :
            return
        print("Ending each run")


if __name__ == "__main__":
    main()
