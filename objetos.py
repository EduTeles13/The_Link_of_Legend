import pygame
import random

class Objetos(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/crystal blue.png')
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(50, 50, 30, 30)
        self.rect.x = random.randint(10,1000)
        self.rect.y = random.randint(50,700)