import pygame as pg
import random

#inicializa o pygame
pg.init()
pg.mixer.init()
pg.font.init()

#importa as bibliotecas necessarias
import config
import funcoes
from veiculo import Veiculo
from raposa import Raposa
from explosao import Explosao


pg.display.set_caption('Foxy Road')
win = pg.display.set_mode((config.WIDTH, config.HEIGHT))

pg.mixer.music.set_volume(config.VOLUME)
musica_jogo = pg.mixer.music.load('sons/musica_do_jogo.mp3')
barulho_pontuacao = pg.mixer.Sound('sons/pontuacao.wav')
pg.mixer.music.play(-1)

clock = pg.time.Clock()
