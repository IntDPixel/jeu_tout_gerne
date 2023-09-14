import pygame
import random


# cree la class comet
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # def l'image comet
        self.image = pygame.image.load('PygameAssets-main/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 5)
        self.rect.x = random.randint(20, 1000)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')
        # verifeir le nb de comets de 0 ou pas
        if len( self.comet_event.all_comets) == 0:
            # remise a 0 event bar
            self.comet_event.reset_percent()
            # appartion 2 monstre
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # tombe sur le sol
        if self.rect.y >= 520:
            self.remove()
            # cherck plus d'autre boule de feu
            if len(self.comet_event.all_comets) == 0:
                print('phase comet finis')
                # remise boucle a 0
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verifier la colison
        if self.comet_event.game.check_collision(
            self,self.comet_event.game.all_players
        ):
            print("joueur touché")
            # retirere la boule
            self.remove()
            # faire subir des degats
            self.comet_event.game.player.damage(20)
