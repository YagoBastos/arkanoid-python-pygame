import pygame
import random
import os


if __name__ == "__main__":

    LARGURA = 800
    ALTURA = 600

    pygame.init()

    pasta_sons = os.path.join(os.path.dirname(__file__), "sons")

    som_colisao_barra = pygame.mixer.Sound(
        os.path.join(pasta_sons, "colisao_barra.wav")
    )
    som_colisao_jogador = pygame.mixer.Sound(
        os.path.join(pasta_sons, "colisao_jogador.wav")
    )
    som_game_over = pygame.mixer.Sound(
        os.path.join(pasta_sons, "game_over.wav")
    )
    som_vitoria = pygame.mixer.Sound(
        os.path.join(pasta_sons, "winner.wav")
    )

    som_colisao_barra.set_volume(0.5)
    som_colisao_jogador.set_volume(0.5)
    som_game_over.set_volume(0.7)
    som_vitoria.set_volume(0.7)

    caminho_musica = os.path.join(
        os.path.dirname(__file__),
        "sons",
        "musica_tema.mp3"
    )
    caminho_musica_jogo = os.path.join(
        os.path.dirname(__file__),
        "sons",
        "game.mp3"
    )
    musica_tema_carregada = False
    musica_jogo_carregada = os.path.exists(caminho_musica_jogo)

    if os.path.exists(caminho_musica):
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        musica_tema_carregada = True

    fonte = pygame.font.Font(None, 36)
    fonte_game_over = pygame.font.Font(None, 60)
    fonte_instrucoes = pygame.font.Font(None, 24)

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

    Invader = [
    "..#.....#..",
    "..#.....#..",
    "...#...#...",
    "...#...#...",
    "..#######..",
    "..#######..",
    ".##.###.##.",
    ".##.###.##.",
    "###########",
    "###########",
    "###########",
    "#.#######.#",
    "#.#.....#.#",
    "#.#.....#.#",
    "...##.##..."
    ]
    Humanoid_DOH = [
    "...........",
    "....###....",
    "....#.#....",
    ".....#.....",
    "....#.#....",
    ".#########.",
    ".#.#####.#.",
    ".#..###....",
    ".#..####...",
    "...#####...",
    "..##...##..",
    "..#....##..",
    "..#....###.",
    ".##........",
    "..........."
    ]

    blocos = [
        "###########",
        "###########",
        "###########",
        "###########",
        "###########",
        "###########",
        "###########",
        "###########"
        
    ]

    # Quantidade de linhas e colunas de blocos.
    quantidade_linhas = 15
    quantidade_colunas = 11

    # Tamanho dos blocos.
    largura_bloco = 45
    altura_bloco = 12

    # Espaço entre os blocos.
    espaco = 5

    largura_grade = (
        quantidade_colunas * largura_bloco
        + (quantidade_colunas - 1) * espaco
    )
    margem_esquerda = (LARGURA - largura_grade) // 2

    def criar_blocos(desenho):
        novos_blocos = []

        for linha, desenho_linha in enumerate(desenho):
            for coluna, simbolo in enumerate(desenho_linha):
                if simbolo != "#":
                    continue

                x = margem_esquerda + coluna * (largura_bloco + espaco)
                y = 50 + linha * (altura_bloco + espaco)

                novos_blocos.append(
                    pygame.Rect(
                        x,
                        y,
                        largura_bloco,
                        altura_bloco
                    )
                )

        return novos_blocos

    def criar_blocos_aleatorios(quantidade):
        novos_blocos = []

        while len(novos_blocos) < quantidade:
            x = random.randint(0, LARGURA - largura_bloco)
            y = random.randint(50, 400)
            novo_bloco = pygame.Rect(
                x,
                y,
                largura_bloco,
                altura_bloco
            )

            if not any(novo_bloco.colliderect(bloco) for bloco in novos_blocos):
                novos_blocos.append(novo_bloco)

        return novos_blocos

    def sortear_saida_bola():
        return (
            random.randint(0, LARGURA - tamanho_bola),
            520,
            random.choice((-5, 5)),
            -5
        )

    # PONTUAÇÃO E ESTADO DO JOGO
    pontuacao = 0
    game_over = False
    ganhou = False
    som_final_tocado = False
    tela_inicial = True
    modo_atual = None
    tempo_ultima_mudanca_blocos = 0
    desenhos = [
        Invader,
        Humanoid_DOH,
        blocos,
        "aleatorio"
    ]

    largura_opcao = 280
    altura_opcao = 90
    espaco_opcao = 20
    inicio_x = (LARGURA - (2 * largura_opcao + espaco_opcao)) // 2
    inicio_y = 180

    def obter_retangulos_opcoes():
        return [
            pygame.Rect(inicio_x, inicio_y, largura_opcao, altura_opcao),
            pygame.Rect(
                inicio_x + largura_opcao + espaco_opcao,
                inicio_y,
                largura_opcao,
                altura_opcao
            ),
            pygame.Rect(
                inicio_x,
                inicio_y + altura_opcao + espaco_opcao,
                largura_opcao,
                altura_opcao
            ),
            pygame.Rect(
                inicio_x + largura_opcao + espaco_opcao,
                inicio_y + altura_opcao + espaco_opcao,
                largura_opcao,
                altura_opcao
            )
        ]


    while executando:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                executando = False

            if (
                evento.type == pygame.MOUSEBUTTONDOWN
                and evento.button == 1
                and tela_inicial
            ):
                for indice, retangulo in enumerate(obter_retangulos_opcoes()):
                    if retangulo.collidepoint(evento.pos):
                        modo_atual = desenhos[indice]
                        if modo_atual == "aleatorio":
                            blocos = criar_blocos_aleatorios(5)
                        else:
                            blocos = criar_blocos(modo_atual)
                        tempo_ultima_mudanca_blocos = pygame.time.get_ticks()
                        x_barra = 350
                        (
                            x_bola,
                            y_bola,
                            velocidade_x,
                            velocidade_y
                        ) = sortear_saida_bola()
                        pontuacao = 0
                        game_over = False
                        ganhou = False
                        som_final_tocado = False
                        if musica_jogo_carregada:
                            pygame.mixer.music.load(caminho_musica_jogo)
                            pygame.mixer.music.play(-1)
                        tela_inicial = False
                        break

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_m:
                    tela_inicial = True
                    game_over = False
                    ganhou = False
                    som_final_tocado = False
                    if musica_tema_carregada:
                        pygame.mixer.music.load(caminho_musica)
                        pygame.mixer.music.play(-1)

                elif (game_over or ganhou) and evento.key == pygame.K_r:

                    # Reposiciona a barra.
                    x_barra = 350

                    # Reposiciona a bola.
                    (
                        x_bola,
                        y_bola,
                        velocidade_x,
                        velocidade_y
                    ) = sortear_saida_bola()

                    # Recupera a direção inicial da bola.
                    # Zera a pontuação.
                    pontuacao = 0

                    # Cria novamente os blocos.
                    if modo_atual == "aleatorio":
                        blocos = criar_blocos_aleatorios(5)
                    else:
                        blocos = criar_blocos(modo_atual)
                    tempo_ultima_mudanca_blocos = pygame.time.get_ticks()

                    # Volta para o jogo.
                    game_over = False
                    ganhou = False
                    som_final_tocado = False
                    if musica_jogo_carregada:
                        pygame.mixer.music.load(caminho_musica_jogo)
                        pygame.mixer.music.play(-1)

        # LEITURA DO TECLADO
        if not tela_inicial and not game_over and not ganhou:

            tempo_atual = pygame.time.get_ticks()
            if (
                modo_atual == "aleatorio"
                and tempo_atual - tempo_ultima_mudanca_blocos >= 2000
            ):
                blocos = criar_blocos_aleatorios(len(blocos))
                tempo_ultima_mudanca_blocos = tempo_atual

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
                som_colisao_barra.play()


            # COLISÃO DA BOLA COM OS BLOCOS
            for bloco in blocos[:]:

                if bola.colliderect(bloco):
                    blocos.remove(bloco)
                    pontuacao += 10
                    velocidade_y *= -1
                    som_colisao_jogador.play()
                    break

            if not blocos:
                ganhou = True
                if not som_final_tocado:
                    som_vitoria.play()
                    som_final_tocado = True


            # VERIFICAÇÃO DE GAME OVER
            # Se a bola passar pela parte inferior da tela,
            # o jogador perde.
            if y_bola > ALTURA:
                game_over = True
                if not som_final_tocado:
                    som_game_over.play()
                    som_final_tocado = True


        # DESENHO DA TELA
        tela.fill((0, 0, 32))

        if tela_inicial:
            titulo = fonte_game_over.render(
                "ARKANOID",
                True,
                (255, 255, 255)
            )

            instrucoes = [
                "Aumente o volume!",
                "Clique com o mouse no inimigo desejado"
            ]

            opcoes = [
                "Invader",
                "Humanoid DOH",
                "Blocos",
                "Attack"
            ]

            tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 70)))

            for indice, instrucao in enumerate(instrucoes):
                texto_instrucao = fonte_instrucoes.render(
                    instrucao,
                    True,
                    (224, 224, 224)
                )
                tela.blit(
                    texto_instrucao,
                    texto_instrucao.get_rect(
                        center=(LARGURA // 2, 535 + indice * 25)
                    )
                )

            for indice, opcao in enumerate(opcoes):
                retangulo_opcao = obter_retangulos_opcoes()[indice]

                pygame.draw.rect(
                    tela,
                    (48, 208, 48),
                    retangulo_opcao,
                    width=3,
                    border_radius=16
                )

                texto_opcao = fonte.render(
                    opcao,
                    True,
                    (48, 208, 48)
                )
                tela.blit(
                    texto_opcao,
                    texto_opcao.get_rect(center=retangulo_opcao.center)
                )

        else:
            pygame.draw.rect(
                tela,
                (224, 224, 224),
                barra
            )

            pygame.draw.rect(
                tela,
                (255, 48, 48),
                bola
            )

            for bloco in blocos:
                pygame.draw.rect(
                    tela,
                    (48, 208, 48),
                    bloco
                )

            texto_pontuacao = fonte.render(
                f"Pontuação: {pontuacao}",
                True,
                (255, 255, 255)
            )

            tela.blit(texto_pontuacao, (20, 15))

            if game_over:
                texto_game_over = fonte_game_over.render(
                    "GAME OVER",
                    True,
                    (255, 255, 255)
                )

                texto_reiniciar = fonte.render(
                    "R - reiniciar    M - menu",
                    True,
                    (255, 255, 255)
                )

                tela.blit(texto_game_over, (280, 250))
                tela.blit(texto_reiniciar, (270, 320))

            elif ganhou:
                texto_ganhador = fonte_game_over.render(
                    "VOCE GANHOU!",
                    True,
                    (255, 255, 255)
                )

                texto_reiniciar = fonte.render(
                    "R - reiniciar    M - menu",
                    True,
                    (255, 255, 255)
                )

                tela.blit(texto_ganhador, (250, 250))
                tela.blit(texto_reiniciar, (270, 320))


        # ATUALIZAÇÃO DA TELA
        pygame.display.flip()

        # Mantém o jogo em 60 atualizações por segundo.
        clock.tick(60)

    pygame.quit()