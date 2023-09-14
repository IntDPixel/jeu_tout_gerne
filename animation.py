import pygame


# def la class animation
class AnimateSprite(pygame.sprite.Sprite):

    # def les choses a faire a la creation
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"PygameAssets-main/{sprite_name}.png")
        self.images = animations.get(sprite_name)
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.animation = False

    # def une methode pour demarre l'animation
    def star_animation(self):
        self.animation = True

    # def une methode pour animer le sprite
    def animate(self, loop=False):

        # verifier si animation active
        if self.animation:

            # passer à l'image suivante
            self.current_image += 1

            # vérifier si on atteint la fin
            if self.current_image >= len(self.images):
                # remise à 0
                self.current_image = 0

                # check if loop
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# def une nouvelle fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les image dans le dossier
    images = []
    # chelins du dosier dans le sprite
    path = f"PygameAssets-main/{sprite_name}/{sprite_name}"

    # boucler sur chaque image dans chaque dosier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoeyr le contenue de la liste d'image
    return images


# def un dictionaire qui a toutes les images de chaque sprites
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}
