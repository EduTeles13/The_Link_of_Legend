import pygame
from quadrado import Player
from objetos import Objetos
from objetos import Objetos1
from objetos import Objetos2
import random

#inicializando o pygame e criando a janela
pygame.init()
altura = 720
largura = 1080
display = pygame.display.set_mode([largura,altura])
pygame.display.set_caption('Garantir a Nota')

#objects
object_group = pygame.sprite.Group()
objetos_group = pygame.sprite.Group()
objetos_group1 = pygame.sprite.Group()
objetos_group2 = pygame.sprite.Group()

player = Player(object_group)
spawn = random.randint(5,8)
spawn1 = random.randint(5,8)
spawn2 = random.randint(5,8)
for i in range(spawn):
    novo_objeto = Objetos(object_group, objetos_group)
for i in range(spawn1):
    novo_objeto1 = Objetos1(object_group, objetos_group1)
for i in range(spawn2):
    novo_objeto2 = Objetos2(object_group, objetos_group2)

gameLoop = True
clock = pygame.time.Clock()
contagem_cristal = 0
contagem_esmeralda = 0
contagem_rubi = 0

if __name__ == '__main__':
    while gameLoop:
        object_group.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
        collisions = pygame.sprite.spritecollide(player, objetos_group, True, pygame.sprite.collide_mask)
        collisions1 = pygame.sprite.spritecollide(player, objetos_group1, True, pygame.sprite.collide_mask)
        collisions2 = pygame.sprite.spritecollide(player, objetos_group2, True, pygame.sprite.collide_mask)

        #contagem dos objetos
        if collisions:
            contagem_cristal +=1
            print(f'{contagem_cristal} cristal')
        elif collisions1:
            contagem_esmeralda+=1
            print(f'{contagem_esmeralda} esmeralda')
        elif collisions2:
            contagem_rubi += 1
            print(f'{contagem_rubi} rubi')

        if contagem_cristal == spawn and contagem_esmeralda == spawn1 and contagem_rubi == spawn2:
            gameLoop = False


        display.fill([0,0,0])
        object_group.update()
        object_group.draw(display)
        pygame.display.update()