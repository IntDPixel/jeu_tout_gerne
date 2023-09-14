import pygame
import math
from game import Game
pygame.init()

# def une clock
clock = pygame.time.Clock()
FPS = 60


# la fenetre du jeu
pygame.display.set_caption("the shooter game")
screen = pygame.display.set_mode((1080, 720))

# importer l'arrier plan
background = pygame.image.load('PygameAssets-main/bg.jpg')

game = Game()

running = True
while running:

    # applique l'arriere plan
    screen.blit(background, (0, -200))

    # charger la banniere
    banner = pygame.image.load('PygameAssets-main/banner.png')
    banner = pygame.transform.scale(banner, (500, 500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 4)

    # importe le bouton de chargement
    play_button = pygame.image.load('PygameAssets-main/button.png')
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3.3)
    play_button_rect.y = math.ceil(screen.get_height() / 2)
    # check debut de partie
    if game.is_playing:
        # declanche les instructions
        game.update(screen)
    # jeu pas commencer
    else:
        # ajouter ecran
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour
    pygame.display.flip()

    # pour fermer la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter touche clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detect la touche espace pour lancer le projectil
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en marche
                    game.start()
                    # jouer le son en question
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # appuiye enclanche
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en marche
                game.start()
                # jouer le son en question
                game.sound_manager.play('click')
    # fixer le nb de fps
    clock.tick(FPS)
