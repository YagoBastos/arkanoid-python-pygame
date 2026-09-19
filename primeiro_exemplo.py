import pygame
from pprint import pprint

if __name__ == "__main__":
    LARGURA = 800
    ALTURA = 600
    pygame.init()

    fonte = pygame.font.Font(None, 36)
    mensagem = ""

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Primeiro Jogo PyGame")

    executando = True

    clock = pygame.time.Clock()

    x_retangulo = 100
    y_retangulo = 100

    while executando:
        #tratando eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        #Leitura do Teclado
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_LEFT]:
            print("seta esquerda")
            x_retangulo -= 10
        
        if teclas[pygame.K_RIGHT]:
            print("seta direita")
            x_retangulo += 10

        if teclas[pygame.K_UP]:
            print("seta para cima")
            y_retangulo -= 10
        
        if teclas[pygame.K_DOWN]:
            print("seta para baixo")
            y_retangulo += 10

        #preechendo o fundo da janela
        tela.fill((0xB8, 0x7A, 0xFF))

        carro = pygame.Rect(x_retangulo, y_retangulo, 150,100)
        linha = pygame.Rect(750,0,1,600)
        pygame.draw.rect(tela,(0x88,0x00,0x00),carro,5)
        pygame.draw.line(tela, (0x00,0x00,0x00),(750,0),(750,600),5)
        if carro.colliderect(linha):
            print("Chegou no final")
            x_retangulo = 600
            mensagem = "Você BATEU!!"
            texto = fonte.render(mensagem, True, "Black")
            tela.blit(texto, (30,30))

        #atualiza a tela
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()