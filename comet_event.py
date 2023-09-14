import pygame
from comet import Comet


# cree une classe
class CometFallEvent:

    # chargement creer compteur et nb
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 15
        self.game = game
        self.fall_mode = False

        # stoker les comets
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle de valeur entre 1 et 10
        for i in range(1, 12):
        # appartition de comets
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # si la jauge est plein
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de comet")
            self.meteor_fall()
            self.fall_mode = True

    def uptade_bar(self, surface):

        # incremente
        self.add_percent()

        # bar d'arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, surface.get_height() - 20, surface.get_width(), 10
        ])
        # bar de chargement
        pygame.draw.rect(surface, (187, 11, 11), [
            0, surface.get_height() - 20, surface.get_width() / 100 * self.percent, 10
        ])
