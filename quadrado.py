import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/pixil-frame-0.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(50, 50, 50, 50)

    def update(self, *args):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_w]:
            self.rect.y -= 5
        elif tecla[pygame.K_s]:
            self.rect.y += 5
        elif tecla[pygame.K_a]:
            self.rect.x -= 5
        elif tecla[pygame.K_d]:
            self.rect.x += 5
            #não passar do limite da tela
        if self.rect.top < 50:
            self.rect.top=50
        elif self.rect.bottom>720:
            self.rect.bottom = 720
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1080:
            self.rect.right = 1080

