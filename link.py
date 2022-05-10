import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sprites_frente = []
        self.sprites_frente.append(pygame.image.load('data/link de frente/link-frente-parado.png'))
        self.sprites_frente.append(pygame.image.load('data/link de frente/link-frente-andando1.png'))
        self.sprites_frente.append(pygame.image.load('data/link de frente/link-frente-andando2.png'))
        self.sprites_frente.append(pygame.image.load('data/link de frente/link-frente-andando3.png'))
        self.sprites_frente.append(pygame.image.load('data/link de frente/link-frente-andando4.png'))
        self.sprites_lado_esquerdo = []
        self.sprites_lado_esquerdo.append(pygame.image.load('data/link esquerda/link-parado-esquerda.png'))
        self.sprites_lado_esquerdo.append(pygame.image.load('data/link esquerda/link-andando-esquerda1.png'))
        self.sprites_lado_esquerdo.append(pygame.image.load('data/link esquerda/link-andando-esquerda2.png'))
        self.sprites_lado_esquerdo.append(pygame.image.load('data/link esquerda/link-andando-esquerda3.png'))
        self.sprites_lado_direito = []
        self.sprites_lado_direito.append(pygame.image.load('data/link direita/link-parado-direita.png'))
        self.sprites_lado_direito.append(pygame.image.load('data/link direita/link-andando-direita1.png'))
        self.sprites_lado_direito.append(pygame.image.load('data/link direita/link-andando-direita2.png'))
        self.sprites_lado_direito.append(pygame.image.load('data/link direita/link-andando-direita3.png'))
        self.sprites_costas = []
        self.sprites_costas.append(pygame.image.load('data/link costa/link-parado-costa.png'))
        self.sprites_costas.append(pygame.image.load('data/link costa/link-andando-costa1.png'))
        self.sprites_costas.append(pygame.image.load('data/link costa/link-andando-costa2.png'))
        self.sprites_costas.append(pygame.image.load('data/link costa/link-andando-costa3.png'))
        self.sprites_ataque_frente = []

        self.atual = 0
        self.image = self.sprites_frente[self.atual]
        self.image = pygame.transform.scale(self.image, [70, 85])
        self.rect = pygame.Rect(50, 50, 50, 50)

    def update(self, *args):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w]:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites_costas):
                self.atual = 0
            self.image = self.sprites_costas[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [70, 85])
            if self.rect.top == 400 and self.rect.right < 350:
                self.rect.y -= 0
            elif self.rect.top == 280 and 300 < self.rect.right < 845:
                self.rect.y -= 0
            elif self.rect.top == 500 and 450 < self.rect.right < 865:
                self.rect.y -= 0
            else:
                self.rect.y -= 1
        if tecla[pygame.K_s]:
            if self.rect.bottom == 375 and self.rect.right < 300:
                self.rect.y += 0
            elif self.rect.bottom == 265 and 300 < self.rect.right < 870:
                self.rect.y += 0
            elif self.rect.bottom == 480 and 450 < self.rect.right < 850:
                self.rect.y += 0
            else:
                self.rect.y += 1
            self.atual = self.atual+0.05
            if self.atual >= len(self.sprites_frente):
                self.atual = 0
            self.image = self.sprites_frente[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [70, 85])
        if tecla[pygame.K_a]:
            if 270 < self.rect.bottom < 450 and self.rect.left == 285:
                self.rect.x -= 0
            elif 270 < self.rect.bottom < 550 and self.rect.left == 795:
                self.rect.x -= 0
            else:
                self.rect.x -= 1
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites_lado_esquerdo):
                self.atual = 0
            self.image = self.sprites_lado_esquerdo[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [70, 85])
        if tecla[pygame.K_d]:
            if 280 < self.rect.bottom < 470 and self.rect.right == 275:
                self.rect.x += 0
            elif 280 < self.rect.bottom < 570 and self.rect.right == 785:
                self.rect.x += 0
            elif 480 < self.rect.bottom < 560 and self.rect.right == 435:
                self.rect.x += 0
            else:
                self.rect.x += 1
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites_lado_direito):
                self.atual = 0
            self.image = self.sprites_lado_direito[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [70, 85])
        if tecla[pygame.K_d] and tecla[pygame.K_a]:
            self.image = self.sprites_frente[0]
            self.image = pygame.transform.scale(self.image, [70, 80])
        if tecla[pygame.K_d] and tecla[pygame.K_a] and tecla[pygame.K_w]:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites_costas):
                self.atual = 0
            self.image = self.sprites_costas[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [70, 85])
        if tecla[pygame.K_d] and tecla[pygame.K_a] and tecla[pygame.K_s]:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites_frente):
                self.atual = 0
            self.image = self.sprites_frente[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [70, 85])
        if tecla[pygame.K_w] and tecla[pygame.K_s]:
            self.image = self.sprites_costas[0]
            self.image = pygame.transform.scale(self.image, [70, 80])

            #não passar do limite da tela
        if self.rect.top < 50:
            self.rect.top=50
        if self.rect.bottom>720:
            self.rect.bottom = 720
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1080:
            self.rect.right = 1080