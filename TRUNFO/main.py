import pygame
import pygame as pyg
from random import randint

pyg.init()
lado = 720
comprimento = 1280
tela = pyg.display.set_mode((comprimento,lado))
tela2 = pyg.display.set_mode((comprimento,lado))
pyg.display.set_caption( "TRUNFO" )
tab = pyg.image.load("data/init1.png")
tab2 = pyg.image.load("data/tab1.png")
start = pyg.image.load("data/startt.png")
regras = pyg.image.load("data/rules.png")
r = pyg.image.load("data/r.png")
info = pyg.image.load("data/infos.png")
back = pyg.image.load("data/backk.png")
verso = pyg.image.load("data/cards/card_verso2.png")
cardii = pyg.image.load("data/cards/ertantan.png")
vazio = pyg.image.load("data/cards/sem_nada.png")
vazio1 = pyg.image.load("data/cards/sem_nada1.png")
pontos1 = 0
pontos2 = 0
fonte = pygame.font.SysFont('arial', 40, True)
c_1 = pyg.image.load("data/cards/c_1.png")
c_2 = pyg.image.load("data/cards/c_2.png")
c_3 = pyg.image.load("data/cards/c_3.png")
c_4 = pyg.image.load("data/cards/c_4.png")
c_5 = pyg.image.load("data/cards/c_5.png")
c_6 = pyg.image.load("data/cards/c_6.png")
c_7 = pyg.image.load("data/cards/c_7.png")
c_8 = pyg.image.load("data/cards/c_8.png")
c_9 = pyg.image.load("data/cards/c_9.png")
c_10 = pyg.image.load("data/cards/c_10.png")
c_11 = pyg.image.load("data/cards/c_11.png")
c_12 = pyg.image.load("data/cards/c_12.png")
c_13 = pyg.image.load("data/cards/c_13.png")
c_14 = pyg.image.load("data/cards/c_14.png")
c_15 = pyg.image.load("data/cards/c_15.png")
c_16 = pyg.image.load("data/cards/c_16.png")
c_17 = pyg.image.load("data/cards/c_17.png")
c_18 = pyg.image.load("data/cards/c_18.png")
c_19 = pyg.image.load("data/cards/c_19.png")
c_20 = pyg.image.load("data/cards/c_20.png")
baralho = [c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9,c_10,c_11,c_12,c_13,c_14,c_15,c_16,c_17,c_18,c_19,c_20]
velocidade = [200, 135, 140, 130, 145, 340, 440, 350, 310, 260, 170, 160, 175, 165, 185, 180, 150, 155, 195, 190]
tecnologia = [30, 18, 12, 22, 20, 98, 94, 88, 96, 150, 48, 14, 52, 44, 56, 50, 16, 26, 70, 74]
funcionalidade = [90, 44, 36, 120, 40, 24, 22, 26, 96, 80, 52, 50, 54, 48, 60, 84, 82, 78, 100, 98]
rod = [0,2,4]
sorteio = 1 #randint(1, 2)
baralhoj2 = []
baralhoj1 = []
while len(baralhoj1) != 6:
    k = randint(0, 19)
    if k not in baralhoj1:
        baralhoj1.append(k)
while len(baralhoj2) != 6:
    k = randint(0, 19)
    if k not in baralhoj2:
        if k not in baralhoj1:
            baralhoj2.append(k)
def tela_i():
    tela.blit(tab, (0, 0))
    tela.blit(start, (600, 260))
    tela.blit(regras, (600, 300))
    tela.blit(info, (600, 340))
    pyg.display.update()

Start = False
gameLoop = True
Menu = True
tela_i()
while gameLoop:
    while Menu:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                gameLoop = False
                Menu = False
            if event.type == pyg.MOUSEBUTTONDOWN:
                x = pyg.mouse.get_pos()[0]
                y = pyg.mouse.get_pos()[1]
                if (x > 15 and y > 15 and x < 120 and y < 55):
                    tela_i()
                if (x > 600 and y > 300 and x < 705 and y < 340):
                    tela.blit(tab2, (0, 0))
                    tela.blit(back, (15, 15))
                    tela.blit(r, (0, 0))
                    pyg.display.update()
                if (x > 600 and y > 340 and x < 705 and y < 380):
                    tela.blit(tab2, (0, 0))
                    tela.blit(back, (15, 15))
                    pyg.display.update()
                if (x > 600 and y > 260 and x < 705 and y < 300):
                    Menu = False
                    tela.blit(tab2, (0, 0))
    for i in range(0,6):
        for j in range(0,1):
            i *= 180
            tela2.blit(verso, (i, j))
    for i in range(0,6):
        for j in range(499,500):
            i *= 180
            tela2.blit(verso, (i, j))
    mensagem1 = f'Jogador1: {pontos1}'
    mensagem2 = f'Jogador2: {pontos2}'
    texto_formatado1 = fonte.render(mensagem1, True, (255, 255, 255))
    texto_formatado2 = fonte.render(mensagem2, True, (255, 255, 255))
    tela.blit(texto_formatado1, (2, 260))
    tela.blit(texto_formatado2, (2, 370))
    if (sorteio == 1):
        b = 0
        i = 0
        for p in range(3):
            rodada = 0
            c = baralhoj1[i]
            d = baralhoj2[i]
            j = i * 180
            tela2.blit(vazio, (j, 0))
            tela2.blit(baralho[c], (475, 210))
            if event.type == pyg.MOUSEBUTTONDOWN:
                if (x > 505 and y > 370 and x < 685 and y < 401):
                    c = baralhoj2[b]
                    print(b,c)
                    tela2.blit(vazio, (j, 500))
                    tela2.blit(baralho[c], (792, 210))
                if (x > 505 and y > 405 and x < 685 and y < 436):
                    c = baralhoj2[b]
                    tela2.blit(vazio, (j, 500))
                    tela2.blit(baralho[c], (792, 210))
                if (x > 505 and y > 440 and x < 685 and y < 471):
                    c = baralhoj2[b]
                    tela2.blit(vazio, (j, 500))
                    tela2.blit(baralho[c], (792, 210))
            tela2.blit(vazio, (j, 500))
            if (rodada == 1):
                c = baralhoj1[b + 1]
                j = i * 180
                tela2.blit(vazio, (j, 500))
                tela2.blit(vazio1, (475, 210))
                tela2.blit(baralho[c], (792, 210))
                i += 1
                if (x > 822 and y > 370 and x < 1002 and y < 401):
                    c = baralhoj2[b + 1]
                    tela2.blit(vazio, (j, 0))
                    tela2.blit(baralho[c], (475, 210))
                    b += 2
                    i += 1
                if (x > 822 and y > 405 and x < 1002 and y < 436):
                    comparador1 = tecnologia[c]
                    c = baralhoj2[b + 1]
                    tela2.blit(vazio, (j, 0))
                    tela2.blit(baralho[c], (475, 210))
                    b += 2
                    i += 1
                if (x > 822 and y > 440 and x < 1002 and y < 471):
                    comparador1 = funcionalidade[c]
                    c = baralhoj2[b + 1]
                    tela2.blit(vazio, (j, 0))
                    tela2.blit(baralho[c], (475, 210))
                    b += 2
                    i += 1

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            gameLoop = False
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_SPACE:
                rodada = 1
                print("Funciona")
        if event.type == pyg.MOUSEBUTTONDOWN:
            x = pyg.mouse.get_pos()[0]
            y = pyg.mouse.get_pos()[1]
            if (x > 505 and y > 370 and x < 685 and y < 401):
                comparador1 = velocidade[c]
                comparador2 = velocidade[d]
                print(comparador1,comparador2)
                if comparador1 > comparador2:
                    pontos1 += comparador1
                    pontos2 -= comparador1 - comparador2
                elif comparador1 < comparador2:
                    pontos2 += comparador2
                    pontos1 -= comparador2 - comparador1
            if (x > 505 and y > 405 and x < 685 and y < 436):
                comparador1 = tecnologia[c]
                comparador2 = tecnologia[d]
                if comparador1 > comparador2:
                    pontos1 += comparador1
                    pontos2 -= comparador1 - comparador2
                else:
                    pontos2 += comparador2
                    pontos1 -= comparador2 - comparador1
            if (x > 505 and y > 440 and x < 685 and y < 471):
                comparador1 = funcionalidade[c]
                comparador2 = funcionalidade[d]
                if comparador1 > comparador2:
                    pontos1 += comparador1
                    pontos2 -= comparador1 - comparador2
                else:
                    pontos2 += comparador2
                    pontos1 -= comparador2 - comparador1
            if (x > 822 and y > 370 and x < 1002 and y < 401):
                comparador2 = velocidade[c]
                comparador1 = velocidade[c]
                if comparador2 > comparador1:
                    pontos2 += comparador1
                    pontos1 -= comparador2 - comparador1
                else:
                    pontos1 += comparador1
                    pontos1 -= comparador1 - comparador2
            if (x > 822 and y > 405 and x < 1002 and y < 436):
                comparador2 = tecnologia[c]
                comparador1 = tecnologia[c]
                if comparador2 > comparador1:
                    pontos2 += comparador1
                    pontos1 -= comparador2 - comparador1
                else:
                    pontos1 += comparador1
                    pontos1 -= comparador1 - comparador2
            if (x > 822 and y > 440 and x < 1002 and y < 471):
                comparador2 = funcionalidade[c]
                comparador1 = funcionalidade[c]
                if comparador2 > comparador1:
                    pontos2 += comparador1
                    pontos1 -= comparador2 - comparador1
                else:
                    pontos1 += comparador1
                    pontos1 -= comparador1 - comparador2


    pyg.display.flip()