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

    #Tela do jogo
    elif tela == 'tela de jogo':
        fundo = pg.sprite.Group()
        fundo.add(funcoes.sprite_fundo('imagens/fundos/mapa.png'))
        
        # Config dos veiculos 
        veiculos = pg.sprite.Group()
        veiculos.add(Veiculo("carro2", vel=4,  x=260))
        veiculos.add(Veiculo("carro1", vel=-7, x=370))
        veiculos.add(Veiculo("carro3", vel=-5, x=873))
        veiculos.add(Veiculo("barco",  vel=3,  x=632))
        veiculos.add(Veiculo("trem",   vel=6,  x=1095))

        # Adiciona a classe da explosao
        explosao = Explosao()

        # Config Raposinha
        personagens = pg.sprite.Group()
        raposinha = Raposa(50, config.HEIGHT / 2)
        personagens.add(raposinha)

        # Config maca
        macas = pg.sprite.Group()
        macazinha= funcoes.cria_item('maca', width=70, height=100, x=1225, y=config.HEIGHT/2)
        macas.add(macazinha)

        # Config cesta 
        cestas = pg.sprite.Group()
        cestinha= funcoes.cria_item('cesta', width=70, height=100, x=75, y=config.HEIGHT/2)

        # Score comeca com valor nulo
        score = 0


        # Loop da tela de jogo
        while tela == 'tela de jogo':
            
            # Adiciona os componentes no jogo
            fundo.draw(win)
            veiculos.draw(win)
            personagens.draw(win)
            macas.draw(win)
            cestas.draw(win)

            veiculos.update()
            personagens.update()
            macas.update()
            cestas.update()
            # Checa colisao da raposinha com veiculos
            if raposinha.checkCollision(veiculos):
                raposinha.kill()
                explosao.explode(win, raposinha.x, raposinha.y)

                tela = 'tela de derrota'

            # Checa colisao da raposinha com a maca e adiciona a cesta  
            for maca in raposinha.checkCollision(macas):
                maca.kill()
                barulho_pontuacao.play()
                cestinha.rect.y = random.randint(100,550)
                cestas.add(cestinha)

            # Checa colisao da raposinha com a cesta, adiciona a maca e atualiza o score
            for cesta in raposinha.checkCollision(cestas):
                cesta.kill()
                barulho_pontuacao.play()
                macazinha.rect.y = random.randint(100,550)
                macas.add(macazinha)

                score+=1
                
                # Atualiza a velocidade dos veiculos em 20% a mais
                for veiculo in veiculos:
                    veiculo.vel *= 1.2
                
                # Atualiza a velocidade da raposa em 20% a mais
                raposinha.vel *= 1.2
                    
            # Pygame   
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    tela = -1
                    break
            
            # Placar do jogo
            funcoes.placar(win, score, 50, 50)

            clock.tick(60)
            pg.display.update()