import pygame
import random
import animation


# class de monstre
class Monster(animation.AnimateSprite):

    # def init est le constructeur
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(-50, 300)
        self.rect.y = 540 - offset
        self.velocity = random.randint(1, 3)
        self.loot_amount = 10
        self.star_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # degat infliger
        self.health -= amount

        # point de vie du monstre
        if self.health <= 0:
            # supprimer le monstre ou  reapartion
            self.rect.x = 1000 + random.randint(-50, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # ajouter le number de point
            self.game.add_score(self.loot_amount)

        # bar d'event chager
        if self.game.comet_event.is_full_loaded():
            # retirer les monstres
            self.game.all_monsters.remove(self)

            # declancher essaie
            self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # dessiner la barre
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # deplacement si non collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
# si le montre en collision avec le joueur
        else:
            # degats au joueur
            self.game.player.damage(self.attack)


# def une classe pour la mummy
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)


# def l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 120)
        self.health = 250
        self.max_health = 250
        self.set_loot_amount(80)
        self.set_speed(1)
        self.attack = 1
