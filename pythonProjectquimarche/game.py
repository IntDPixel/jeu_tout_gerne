import pygame


class Game:

    def __int__(self):

        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("mon premier jeu")

    def run():

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


pygame.init()
Game.run()
