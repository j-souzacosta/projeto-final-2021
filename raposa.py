#importa as bibliotecas necessarias
import pygame as pg
import config

#Classe da raposa
class Raposa(pg.sprite.Sprite):
    #posicoes e velociade da raposa
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

    #update de posicao
    def update(self):
        self.movement()
        self.correction()
        self.rect.center = (self.x, self.y)

    #movimentos da raposinha e atualizacao das imagens dependendo do movimento
    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x -= self.vel

            if self.flip > 0:
                self.flip = -1
                self.image = pg.transform.flip(self.image, True, False)

        elif keys[pg.K_RIGHT]:
            self.x += self.vel

            if self.flip < 0:
                self.flip = 1
                self.image = pg.transform.flip(self.image, True, False)

        if keys[pg.K_UP]:
            self.y -= self.vel

        elif keys[pg.K_DOWN]:
            self.y += self.vel

    def correction(self):
        if self.x - self.width / 2 < 0:
            self.x = self.width / 2

        elif self.x + self.width / 2 > config.WIDTH:
            self.x = config.WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2

        elif self.y + self.height / 2 > config.HEIGHT:
            self.y = config.HEIGHT - self.height / 2

    #checagem de colisao
    def checkCollision(self, group):
        collision = pg.sprite.spritecollide(self, group, False, pg.sprite.collide_mask)

        return collision