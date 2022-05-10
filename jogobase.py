import pygame
from link import Player
from objetos import Objetos
import random

# ----------------------------------------- #
# Inicializando o pygame e criando a janela #
# ----------------------------------------- #

pygame.init()
altura = 720
largura = 1080
display = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('The Legend of Link')
bg = pygame.image.load("data/Mapa_1.png")

# ---------------- #
# Grupo de objetos #
# ---------------- #

object_group = pygame.sprite.Group()
objetos_group = pygame.sprite.Group()
objetos_group1 = pygame.sprite.Group()
objetos_group2 = pygame.sprite.Group()
player = Player(object_group)

# ------------ #
# Start Screen #
# ------------ #

link_menu = pygame.image.load('data/linktela.png').convert_alpha()
link_menu = pygame.transform.rotozoom(link_menu, 0, 0.5)
link_menu_rect = link_menu.get_rect(center=(540, 360))


def start_menu():
    vitoria_txt = test_font.render('Parabens, voce venceu ! ! ', False, (64, 64, 64))
    vitoria_txt_rect = vitoria_txt.get_rect(center=(540, 70))

    game_title = test_font.render("THE LEGEND OF LINK", False, (64, 64, 64))
    game_title_rect = game_title.get_rect(center=(540, 70))

    start_space = test_font.render("Aperte space para jogar", False, (64, 64, 64))
    start_space_rect = start_space.get_rect(center=(540, 650))

    end_space = test_font.render("Aperte space para jogar de novo", False, (64, 64, 64))
    end_space_rect = end_space.get_rect(center=(540, 650))

    if gameover:
        display.blit(vitoria_txt, vitoria_txt_rect)
        display.blit(end_space, end_space_rect)
    else:
        display.blit(game_title, game_title_rect)
        display.blit(start_space, start_space_rect)


# ------------------ #
# Spawn dos cristais #
# ------------------ #

def spawn_objetos():
    global spawn, spawn1, spawn2, contagem_rubi, contagem_cristal, contagem_esmeralda
    spawn = random.randint(5, 8)
    spawn1 = random.randint(5, 8)
    spawn2 = random.randint(5, 8)

    for i in range(spawn):
        novo_objeto = Objetos(object_group, objetos_group)
    for i in range(spawn1):
        novo_objeto1 = Objetos(object_group, objetos_group1)
        novo_objeto1.image = pygame.image.load('data/esmeralda.png')
        novo_objeto1.image = pygame.transform.scale(novo_objeto1.image, [30, 30])
    for i in range(spawn2):
        novo_objeto2 = Objetos(object_group, objetos_group2)
        novo_objeto2.image = pygame.image.load('data/escarlate.png')
        novo_objeto2.image = pygame.transform.scale(novo_objeto2.image, [30, 30])


contagem_esmeralda = 0
contagem_rubi = 0
contagem_cristal = 0

# ----------------------- #
# Desenha valores na tela #
# ----------------------- #

test_font = pygame.font.Font('data/Pixeltype.ttf', 50)
fonte = pygame.font.Font(None, 35)

texto = fonte.render("esmeralda:" + str(contagem_esmeralda), True, (255, 255, 255), None)
texto1 = fonte.render("diamante:" + str(contagem_rubi), True, (255, 255, 255), None)
texto2 = fonte.render("rubi:" + str(contagem_cristal), True, (255, 255, 255), None)

# ----------------------- #
# Som de fundo e cristais #
# ----------------------- #

pygame.mixer.music.load('data/saria_arrocha.mp3')
pygame.mixer.music.play(-1)
barulho_cristal = pygame.mixer.Sound('data/sell_buy_item.wav')


# ===================== gameloop ======================== #

gameover = False
gameLoop = True
game_active = False

clock = pygame.time.Clock()

if __name__ == '__main__':
    while gameLoop:
        clock.tick(120)
        # -----fila-de-eventos----- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            if event.type == pygame.KEYDOWN and not game_active:
                if event.key == pygame.K_SPACE:
                    gameover = False
                    game_active = True
                    spawn_objetos()
                    contagem_rubi = 0
                    texto2 = fonte.render("rubi:" + str(contagem_rubi), True, (255, 255, 255), None)
                    contagem_cristal = 0
                    texto1 = fonte.render("diamante:" + str(contagem_cristal), True, (255, 255, 255), None)
                    contagem_esmeralda = 0
                    texto = fonte.render("esmeralda:" + str(contagem_esmeralda), True, (255, 255, 255), None)

        if game_active:
            object_group.update()
            display.blit(bg, (0, 0))

            # ----- desenha na tela -----#

            display.blit(texto, [0, 0])
            display.blit(texto1, [400, 0])
            display.blit(texto2, [900, 0])

            if not gameover:
                collisions = pygame.sprite.spritecollide(player, objetos_group, True, pygame.sprite.collide_mask)
                collisions1 = pygame.sprite.spritecollide(player, objetos_group1, True, pygame.sprite.collide_mask)
                collisions2 = pygame.sprite.spritecollide(player, objetos_group2, True, pygame.sprite.collide_mask)

                # ---- contagem dos objetos ---- #

                if collisions:
                    barulho_cristal.play()
                    contagem_cristal += 1
                    texto1 = fonte.render("diamante:" + str(contagem_cristal), True, (255, 255, 255), None)
                elif collisions1:
                    barulho_cristal.play()
                    contagem_esmeralda += 1
                    texto = fonte.render("esmeralda:" + str(contagem_esmeralda), True, (255, 255, 255), None)
                elif collisions2:
                    barulho_cristal.play()
                    contagem_rubi += 1
                    texto2 = fonte.render("rubi:" + str(contagem_rubi), True, (255, 255, 255), None)

                if contagem_cristal == spawn and contagem_esmeralda == spawn1 and contagem_rubi == spawn2:
                    gameover = True
                    game_active = False

        else:
            display.fill((111, 184, 108))
            display.blit(link_menu, link_menu_rect)
            start_menu()

        if game_active:
            object_group.update()
            object_group.draw(display)
        pygame.display.update()
