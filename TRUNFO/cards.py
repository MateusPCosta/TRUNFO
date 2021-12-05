import pygame as pyg

c_1 = pyg.image.load("data/cards/c_1.png")
c_2 = pyg.image.load("data/cards/c_2.png")
c_3 = pyg.image.load("data/cards/c_3.png")
c_4 = pyg.image.load("data/cards/c_4.png")
c_5 = pyg.image.load("data/cards/c_5.png")
c_6 = pyg.image.load("data/cards/c_6.png")
c_7 = pyg.image.load("data/cards/c_7.png")
c_8 = pyg.image.load("data/cards/c_8.png")
c_9 = pyg.image.load("data/cards/c_9.png")

baralho = [c_1,c_2,c_3,c_4,c_5,c_6,c_7,c_8,c_9]

for v in range(4):
    tela2.blit(verso, (l, m))
    conteudo = None
    l += 180
l = 0
m = 360
for v in range(4):
    tela2.blit(verso, (l, m))
    conteudo = None
    l += 180

def segunda jogada1():
    for i in range(0, 1):
        for j in range(0, 1):
            c = baralhoj2[i]
            tela2.blit(vazio, (i, j))
            tela2.blit(baralho[c], (300, 210))

c = baralhoj1[i+1]
            tela2.blit(vazio, (i, 500))
            tela2.blit(baralho[c], (792, 210))
            if (x > 505 and y > 370 and x < 685 and y < 401):
                comparador1 = velocidade[c]
                print("Funciona")
            if (x > 505 and y > 405 and x < 685 and y < 436):
                comparador1 = tecnologia[c]
                print("Funciona1")
            if (x > 505 and y > 440 and x < 685 and y < 471):
                comparador1 = funcionalidade[c]
                print("Funciona2")
                c = baralhoj2[i+1]
                tela2.blit(vazio, (i, 0))
                tela2.blit(baralho[c], (475, 210))

if (sorteio == 1):
    b = 0
    i = 0
    for p in range(3):
        rodada = 0
        print(b)
        c = baralhoj1[i]
        d = baralhoj2[i]
        j = i * 180
        tela2.blit(vazio, (j, 0))
        tela2.blit(baralho[c], (475, 210))
        if (x > 505 and y > 370 and x < 685 and y < 401):
            comparador1 = velocidade[c]
            comparador2 = velocidade[d]
            c = baralhoj2[b]
            tela2.blit(vazio, (j, 500))
            tela2.blit(baralho[c], (792, 210))
            if comparador1 > comparador2:
                pontos1 += comparador1
                pontos2 -= comparador1 - comparador2
            else:
                pontos2 += comparador2
                pontos1 -= comparador2 - comparador1
            rodada = 1
        if (x > 505 and y > 405 and x < 685 and y < 436):
            comparador1 = tecnologia[c]
            comparador2 = tecnologia[d]
            c = baralhoj2[b]
            tela2.blit(vazio, (j, 500))
            tela2.blit(baralho[c], (792, 210))
            if comparador1 > comparador2:
                pontos1 += comparador1
                pontos2 -= comparador1 - comparador2
            else:
                pontos2 += comparador2
                pontos1 -= comparador2 - comparador1
            rodada = 1
        if (x > 505 and y > 440 and x < 685 and y < 471):
            comparador1 = funcionalidade[c]
            comparador2 = funcionalidade[d]
            print(comparador1, comparador2)
            c = baralhoj2[b]
            tela2.blit(vazio, (j, 500))
            tela2.blit(baralho[c], (792, 210))
            if comparador1 > comparador2:
                pontos1 += comparador1
                pontos2 -= comparador1 - comparador2
            else:
                pontos2 += comparador2
                pontos1 -= comparador2 - comparador1
            rodada = 1
        else:
            continue
    if (rodada == 1):
        c = baralhoj1[b + 1]
        j = i * 180
        tela2.blit(vazio, (j, 500))
        tela2.blit(vazio1, (475, 210))
        tela2.blit(baralho[c], (792, 210))
        # i += 1
        if (x > 822 and y > 370 and x < 1002 and y < 401):
            comparador1 = velocidade[c]
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

    if (sorteio == 1):
        i = 0
        b = 0
        for p in range(6):
            c = baralhoj1[i]
            d = baralhoj2[i]
            g = i * 180
            tela2.blit(vazio, (g, 0))
            tela2.blit(baralho[c], (475, 210))
            if event.key == pyg.K_v:
                print("funciona")
                comparador1 = velocidade[c]
                comparador2 = velocidade[d]
                h = baralhoj2[b]
                tela2.blit(vazio, (j, 500))
                tela2.blit(baralho[h], (792, 210))
                if comparador1 > comparador2:
                    pontos1 += comparador1
                    pontos2 -= comparador1 - comparador2
                    pyg.display.update()
                else:
                    pontos2 += comparador2
                    pontos1 -= comparador2 - comparador1