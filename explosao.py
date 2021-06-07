import pygame as pg
import funcoes
import time

barulho_colisao = pg.mixer.Sound('sons/explosao.wav')

#Definindo a explosao
class Explosao(object):
    def __init__(self):
        self.width = 140
        self.height = 140
        self.costume = 1

    #Definindo os frames da explosao
    def explode(self, win, x, y):
        x -= self.width / 2
        y -= self.height / 2

        barulho_colisao.play()

        while self.costume < 9:
            self.image = pg.image.load('imagens/explosao/explosao' + str(self.costume) + '.png')
            self.image = pg.transform.scale(self.image, (self.width, self.height))
            self.costume += 1

            win.blit(self.image, (x, y))
            time.sleep(0.2)
            pg.display.update()