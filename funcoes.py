import pygame as pg
import config

def novo_sprite(image, width, height, x, y):
    fundo_image = pg.image.load(image)
    fundo_sprite = pg.sprite.Sprite()

    fundo_sprite.image = fundo_image
    fundo_sprite.image = pg.transform.scale(fundo_image, (width, height))
    fundo_sprite.rect = fundo_image.get_rect()
    
    fundo_sprite.rect.x = x
    fundo_sprite.rect.y = y

    return fundo_sprite
