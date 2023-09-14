from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
import pygame
import sounds


# cree une nouvelle classe game
class Game:
    def __init__(self):
        # def le debut du jeu
        self.is_playing = False
        # generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # genere l'event
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.sound_manager = sounds.SoundManager()
        # scrore a 0
        self.font = pygame.font.SysFont("monospace", 16)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, point=10):
        self.score += point

    def game_over(self):
        # remise a 0 du jeu
        self.comet_event.all_comets = pygame.sprite.Group()
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):
        # afficher le score sur l'ecran
        score_texte = self.font.render(f"Score :{self.score}", 1, (0, 0, 0))
        screen.blit(score_texte, (20, 20))
        # appliquer l'image du joueur.
        screen.blit(self.player.image, self.player.rect)

        # bar vie du joueur
        self.player.update_health_bar(screen)
        self.player.update_animation()

        # actualiser la bar d'evenement du jeu
        self.comet_event.uptade_bar(screen)

        # recup des project
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupe les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuper les comets
        for comet in self.comet_event.all_comets:
            comet.fall()

        # apliquer l ensemble des imùage de proj
        self.player.all_projectiles.draw(screen)

        # ensemble de monstre
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des image comets
        self.comet_event.all_comets.draw(screen)

        # JOUEUR A GAUCHE OU A DROITE
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
