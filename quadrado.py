import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/pixil-frame-0.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(50, 50, 50, 50)

    def update(self, *args, obstaculo=False):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w]:
            if self.rect.top == 425 and self.rect.right < 355:
                self.rect.y -= 0
            elif self.rect.top == 315 and 300 < self.rect.right < 850:
                self.rect.y -= 0
            elif self.rect.top == 525 and 450 < self.rect.right < 870:
                self.rect.y -= 0
            else:
                self.rect.y -= 5
        if tecla[pygame.K_s]:
            if self.rect.bottom == 375 and self.rect.right < 300:
                self.rect.y += 0
            elif self.rect.bottom == 265 and 300 < self.rect.right < 870:
                self.rect.y += 0
            elif self.rect.bottom == 480 and 450 < self.rect.right < 850:
                self.rect.y += 0
            else:
                self.rect.y += 5
        if tecla[pygame.K_a]:
            if 270 < self.rect.bottom < 470 and self.rect.left == 310:
                self.rect.x -= 0
            elif 270 < self.rect.bottom < 570 and self.rect.left == 820:
                self.rect.x -= 0
            else:
                self.rect.x -= 5
        if tecla[pygame.K_d]:
            if 270 < self.rect.bottom < 470 and self.rect.right == 275:
                self.rect.x += 0
            elif 270 < self.rect.bottom < 570 and self.rect.right == 785:
                self.rect.x += 0
            elif 480 < self.rect.bottom < 560 and self.rect.right == 435:
                self.rect.x += 0
            else:
                self.rect.x += 5
        # não passar do limite da tela
        if self.rect.top < 50:
            self.rect.top = 50
        if self.rect.bottom > 720:
            self.rect.bottom = 720
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1080:
            self.rect.right = 1080
        # não passar dos obstáculos