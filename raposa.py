#importa as bibliotecas necessarias
import pygame as pg
import config

class Raposa(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 100
        self.height = 50
        self.x = x
        self.y = y
        self.vel = 4
        self.flip = 1

        #Images da raposinha
        self.image = pg.image.load('imagens/personagens/raposa.png')
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
