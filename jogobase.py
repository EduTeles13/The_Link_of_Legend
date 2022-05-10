import pygame
from link import Player
from objetos import Objetos
import random

#inicializando o pygame e criando a janela
pygame.init()
altura = 720
largura = 1080
display = pygame.display.set_mode([largura,altura])
pygame.display.set_caption('Garantir a Nota')
bg = pygame.image.load("data/Mapa_1.png")

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
    novo_objeto1 = Objetos(object_group, objetos_group1)
    novo_objeto1.image = pygame.image.load('data/crystal green.png')
    novo_objeto1.image = pygame.transform.scale(novo_objeto1.image, [30, 30])
for i in range(spawn2):
    novo_objeto2 = Objetos(object_group, objetos_group2)
    novo_objeto2.image = pygame.image.load('data/crystal red.png')
    novo_objeto2.image = pygame.transform.scale(novo_objeto2.image, [30, 30])

gameLoop = True
clock = pygame.time.Clock()
contagem_cristal = 0
contagem_esmeralda = 0
contagem_rubi = 0

# tela
fonte = pygame.font.Font(None, 35)
fim_de_jogo = pygame.font.Font(None, 60)
texto = fonte.render("esmeralda:"+str(contagem_esmeralda),True,(255, 255, 255), (0, 0, 0))
texto1 = fonte.render("diamante:"+str(contagem_rubi),True,(255, 255, 255), (0, 0, 0))
texto2 = fonte.render("rubi:"+str(contagem_cristal),True,(255, 255, 255), (0, 0, 0))
FIMDEJOGO = fim_de_jogo.render("parabéns você garantiu o projeto de P1!!!", True, (255, 255, 255), (0, 0, 0))

gameover = False
tecla = pygame.key.get_pressed()
if __name__ == '__main__':
    while gameLoop:
            object_group.update()
            clock.tick(120)
            display.blit(bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False


            if not gameover:
                collisions = pygame.sprite.spritecollide(player, objetos_group, True, pygame.sprite.collide_mask)
                collisions1 = pygame.sprite.spritecollide(player, objetos_group1, True, pygame.sprite.collide_mask)
                collisions2 = pygame.sprite.spritecollide(player, objetos_group2, True, pygame.sprite.collide_mask)

                #contagem dos objetos
                if collisions:
                    contagem_cristal +=1
                    texto1 = fonte.render("diamante:" + str(contagem_cristal), True, (255, 255, 255), (0, 0, 0))
                elif collisions1:
                    contagem_esmeralda+=1
                    texto = fonte.render("esmeralda:" + str(contagem_esmeralda), True, (255, 255, 255), (0, 0, 0))
                elif collisions2:
                    contagem_rubi +=1
                    texto2 = fonte.render("rubi:" + str(contagem_rubi), True, (255, 255, 255), (0, 0, 0))

                if contagem_cristal == spawn and contagem_esmeralda == spawn1 and contagem_rubi == spawn2:
                    gameover = True

                display.blit(texto, [0, 0])
                display.blit(texto1, [400, 0])
                display.blit(texto2, [900, 0])
                if gameover == True:
                    display.blit(FIMDEJOGO, [10, 140])

                object_group.update()
                object_group.draw(display)
                pygame.display.flip()
