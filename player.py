import pygame
import animation
from projectile import Projectile


# creer une nouvelle classe
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 440
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur apas de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # dessiner la barre
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 8])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 8])

    def launch_projectile(self):
        # new instance
        self.all_projectiles.add(Projectile(self))
        # demarrer l'animation
        self.star_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        # si pas de collision
             self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
