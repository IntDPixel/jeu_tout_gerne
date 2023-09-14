import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            'meteorite': pygame.mixer.Sound('PygameAssets-main/sounds/meteorite.ogg'),
            'game_over': pygame.mixer.Sound('PygameAssets-main/sounds/game_over.ogg'),
            'tir': pygame.mixer.Sound('PygameAssets-main/sounds/tir.ogg'),
            'click': pygame.mixer.Sound('PygameAssets-main/sounds/click.ogg')
        }

    def play(self, name):
        self.sounds[name].play()
