import pygame
import random


if __name__ == "__main__":

    LARGURA = 800
    ALTURA = 600

    pygame.init()

    fonte = pygame.font.Font(None, 36)
    fonte_game_over = pygame.font.Font(None, 60)

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Arkanoid")

    executando = True
    clock = pygame.time.Clock()

    # JOGADOR
    x_barra = 350
    y_barra = 550

    largura_barra = 100
    altura_barra = 15

    velocidade_barra = 8


    # BOLA
    x_bola = 390
    y_bola = 520

    tamanho_bola = 15

    velocidade_x = 5
    velocidade_y = -5


    # BLOCOS
    blocos = []

    # Quantidade de linhas e colunas de blocos.
    quantidade_linhas = 4
    quantidade_colunas = 10

    # Tamanho dos blocos.
    largura_bloco = 70
    altura_bloco = 25

    # Espaço entre os blocos.
    espaco = 5

    for linha in range(quantidade_linhas):

        for coluna in range(quantidade_colunas):

            x = 25 + coluna * (largura_bloco + espaco)
            y = 50 + linha * (altura_bloco + espaco)

            bloco = pygame.Rect(
                x,
                y,
                largura_bloco,
                altura_bloco
            )

            blocos.append(bloco)

    # PONTUAÇÃO E ESTADO DO JOGO
    pontuacao = 0
    game_over = False


    while executando:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                executando = False

            # Quando o jogador perde, a tecla R reinicia.
            if game_over and evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_r:

                    # Reposiciona a barra.
                    x_barra = 350

                    # Reposiciona a bola.
                    x_bola = 390
                    y_bola = 520

                    # Recupera a direção inicial da bola.
                    velocidade_x = 5
                    velocidade_y = -5

                    # Zera a pontuação.
                    pontuacao = 0

                    # Cria novamente os blocos.
                    blocos = []

                    for linha in range(quantidade_linhas):

                        for coluna in range(quantidade_colunas):

                            x = 25 + coluna * (largura_bloco + espaco)
                            y = 50 + linha * (altura_bloco + espaco)

                            bloco = pygame.Rect(
                                x,
                                y,
                                largura_bloco,
                                altura_bloco
                            )

                            blocos.append(bloco)

                    # Volta para o jogo.
                    game_over = False

        # LEITURA DO TECLADO
        if not game_over:

            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_LEFT]:

                x_barra -= velocidade_barra

            if teclas[pygame.K_RIGHT]:

                x_barra += velocidade_barra

            if x_barra < 0:
                x_barra = 0

            if x_barra + largura_barra > LARGURA:
                x_barra = LARGURA - largura_barra


            # MOVIMENTAÇÃO DA BOLA
            x_bola += velocidade_x
            y_bola += velocidade_y


            # COLISÃO COM AS PAREDES
            # Se a bola bater na parede esquerda ou direita,
            # invertemos sua velocidade horizontal.
            if x_bola <= 0 or x_bola + tamanho_bola >= LARGURA:

                velocidade_x *= -1

            # Se a bola bater no teto, ela volta para baixo.
            if y_bola <= 0:

                velocidade_y *= -1

            # CRIAÇÃO DOS RETÂNGULOS
            barra = pygame.Rect(
                x_barra,
                y_barra,
                largura_barra,
                altura_barra
            )

            bola = pygame.Rect(
                x_bola,
                y_bola,
                tamanho_bola,
                tamanho_bola
            )


            # COLISÃO DA BOLA COM A BARRA
            if bola.colliderect(barra) and velocidade_y > 0:

                # A bola só muda de direção quando está
                # descendo. Isso evita que ela fique presa
                # dentro da barra.
                velocidade_y *= -1

                # Reposiciona a bola acima da barra.
                y_bola = y_barra - tamanho_bola


            # COLISÃO DA BOLA COM OS BLOCOS
            for bloco in blocos[:]:

                if bola.colliderect(bloco):
                    blocos.remove(bloco)
                    pontuacao += 10
                    velocidade_y *= -1
                    break


            # VERIFICAÇÃO DE GAME OVER
            # Se a bola passar pela parte inferior da tela,
            # o jogador perde.
            if y_bola > ALTURA:
                game_over = True


        # DESENHO DA TELA
        # Limpa a tela.
        tela.fill((20, 20, 30))

        # Desenha o jogador.
        pygame.draw.rect(
            tela,
            (0, 200, 255),
            barra
        )

        # Desenha a bola.
        pygame.draw.rect(
            tela,
            (255, 255, 255),
            bola
        )

        # Desenha todos os blocos restantes.
        for bloco in blocos:

            pygame.draw.rect(
                tela,
                (255, 100, 100),
                bloco
            )


        # PONTUAÇÃO
        texto_pontuacao = fonte.render(
            f"Pontuação: {pontuacao}",
            True,
            (255, 255, 255)
        )

        tela.blit(
            texto_pontuacao,
            (20, 15)
        )


        # GAME OVER
        if game_over:
            texto_game_over = fonte_game_over.render(
                "GAME OVER",
                True,
                (255, 255, 255)
            )

            texto_reiniciar = fonte.render(
                "Pressione R para reiniciar",
                True,
                (255, 255, 255)
            )

            tela.blit(
                texto_game_over,
                (280, 250)
            )

            tela.blit(
                texto_reiniciar,
                (270, 320)
            )


        # ATUALIZAÇÃO DA TELA
        pygame.display.flip()

        # Mantém o jogo em 60 atualizações por segundo.
        clock.tick(60)

    pygame.quit()