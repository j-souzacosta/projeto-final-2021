#importa as bibliotecas necessarias
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

#Configuracoes da tela
pg.display.set_caption('Foxy Road')
win = pg.display.set_mode((config.WIDTH, config.HEIGHT))

#Configuracao dos sons
pg.mixer.music.set_volume(config.VOLUME)
musica_jogo = pg.mixer.music.load('sons/musica_do_jogo.mp3')
barulho_pontuacao = pg.mixer.Sound('sons/pontuacao.wav')
pg.mixer.music.play(-1)

clock = pg.time.Clock()

#Jogo inicializa na tela de inicio
tela = 'tela de inicio'

#Loop do jogo
while True:
    if tela == 'tela de inicio':
        # Inicializa tela inicial
        fundo = pg.sprite.Group()
        fundo.add(funcoes.sprite_fundo('imagens/fundos/home_screen.png'))

        # Loop da tela inicial
        while tela == 'tela de inicio':
            fundo.draw(win)

            # Detecta Teclas
            pressed_keys = pg.key.get_pressed()

            # Tecla ESPACO
            if pressed_keys[pg.K_SPACE]:
                tela = 'tela de animação'

            # Tecla ENTER
            elif pressed_keys[pg.K_RETURN]:
                tela = 'tela de como jogar'
            
            # Pygame
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    tela = -1
                    break

            clock.tick(60)
            pg.display.update()

    #Tela com instrucoes de como jogar 
    elif tela == 'tela de como jogar':
        fundo = pg.sprite.Group()
        fundo.add(funcoes.sprite_fundo('imagens/fundos/how_to_play.png'))

        # Loop da tela de como jogar
        while tela == 'tela de como jogar':
            fundo.draw(win)

            # Detecta Teclas
            pressed_keys = pg.key.get_pressed()

            # Tecla ESC
            if pressed_keys[pg.K_ESCAPE]:
                tela = 'tela de inicio'

            # Pygame
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    tela = -1
                    break

            clock.tick(60)
            pg.display.update()
            
    #Animacao entre a tela inicial e a tela do jogo
    elif tela == 'tela de animação':
        # Inicializa de transição
        logo = funcoes.sprite_fundo('imagens/fundos/home_screen.png')

        fundo = pg.sprite.Group()
        fundo.add(funcoes.sprite_fundo('imagens/fundos/mapa.png'))
        fundo.add(logo)

        # Loop da tela de transição
        while tela == 'tela de animação':
            # Transicao
            for y in range(0, -config.HEIGHT, -10):
                logo.rect.y = y

                fundo.draw(win)

                clock.tick(60)
                pg.display.update()

            tela = 'tela de jogo'