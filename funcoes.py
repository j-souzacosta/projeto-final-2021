#importa as bibliotecas necessarias
import pygame as pg
import config

#Carrega as imagens do jogo
def novo_sprite(image, width, height, x, y):
    fundo_image = pg.image.load(image)
    fundo_sprite = pg.sprite.Sprite()

    fundo_sprite.image = fundo_image
    fundo_sprite.image = pg.transform.scale(fundo_image, (width, height))
    fundo_sprite.rect = fundo_image.get_rect()
    
    fundo_sprite.rect.x = x
    fundo_sprite.rect.y = y

    return fundo_sprite

#Coloca as imagens nas dimensoes do jogo
def sprite_fundo(imagem):
    return novo_sprite(imagem, width=config.WIDTH, height=config.HEIGHT, x=0,  y=0)

#Cria os itens do jogo
def cria_item(item, width, height, x, y):
    imagem = 'imagens/itens/' + item + '.png'
    sprite = novo_sprite(imagem, width=width, height=height, x=x, y=y)

    sprite.rect.x -= width / 2
    sprite.rect.y -= height / 2

    return sprite

#Pontuacao do jogador
score_font = pg.font.SysFont('consolas', 60, True)

#Score na tela do jogo
def scoreDisplay(win, score, x, y):
    score_text = score_font.render(str(score), True, (0, 0, 0))
    win.blit(score_text, (x, y))
