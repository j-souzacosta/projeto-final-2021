#importa as bibliotecas necessarias
import pygame as pg
import config

class Veiculo(pg.sprite.Sprite):
    def __init__(self, vehicle, vel, x):
        super().__init__()

        self.vel = vel

        self.width = 80
        self.height = 200
        self.image = pg.image.load('imagens/veiculos/' + vehicle + '.png')
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.x = x

        if vel > 0:
            self.y = self.height / -2
            self.image = pg.transform.flip(self.image, False, True)
        else:
            self.y = config.HEIGHT + self.height / 2

    #Transforma as variaveis que serao utilizadas para definir os movimentos dos veiculos
    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    #Define a movimentacao dos veiculos
    def movement(self):
        self.y += self.vel

        if self.vel < 0 and self.y <= self.height/-2 :
            self.y = config.HEIGHT + self.height/2

        elif self.vel > 0 and self.rect.top >= config.HEIGHT:
            self.y = self.height/-2
