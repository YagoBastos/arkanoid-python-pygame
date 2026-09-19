# Arkanoid em Python e Pygame

Projeto desenvolvido para a atividade de aula de Desenvolvimento de Jogos. O objetivo foi criar um jogo do tipo **Arkanoid/Breakout** usando Python e a biblioteca Pygame, aplicando conceitos de janela gráfica, eventos de teclado e mouse, movimentação, colisões, pontuação e estados de jogo.

O repositório contém duas versões do mesmo jogo:

- **Arkanoid v1:** versão mais simples, desenvolvida com foco nas mecânicas essenciais da atividade e com uso reduzido de IA.
- **Arkanoid v2:** versão mais avançada, com mais recursos e maior apoio de IA durante o desenvolvimento, buscando melhorar a experiência e o resultado final.

## Requisitos

- Python 3 instalado
- Biblioteca Pygame
- Os arquivos deste repositório, incluindo a pasta `sons`, mantidos na mesma estrutura

## Instalação

No terminal, dentro da pasta do projeto, instale o Pygame:

```bash
python -m pip install pygame
```

## Como executar

Ainda no terminal, use um dos comandos abaixo:

### Versão 1 - simples

```bash
python Arkanoid_v1.py
```

### Versão 2 - avançada

```bash
python Arkanoid_v2.py
```

## Controles

### Arkanoid v1

- `Seta esquerda` / `Seta direita`: movimentam a barra.
- `R`: reinicia a partida depois do Game Over.
- Fechar a janela: encerra o jogo.

### Arkanoid v2

- Clique do mouse: escolhe uma formação de blocos no menu inicial.
- `Seta esquerda` / `Seta direita`: movimentam a barra.
- `R`: reinicia a partida depois do Game Over ou da vitória.
- `M`: retorna ao menu inicial.
- Fechar a janela: encerra o jogo.

## Funcionalidades implementadas

As duas versões possuem as principais mecânicas solicitadas no enunciado:

- movimentação da barra pelo teclado;
- movimentação automática da bola;
- colisão da bola com as paredes, a barra e os blocos;
- remoção dos blocos atingidos;
- pontuação exibida na janela do jogo;
- indicação de Game Over;
- reinício da partida sem fechar o programa;
- código comentado nos trechos principais e organizado com nomes descritivos.

Além dos requisitos mínimos, a **versão 2** possui:

- menu inicial para escolher a formação de blocos;
- formações inspiradas em `Invader` e `Humanoid DOH`;
- formação tradicional e formação aleatória;
- condição de vitória quando todos os blocos são destruídos;
- efeitos sonoros para colisões, vitória e Game Over;
- músicas de menu e de partida;
- opção de retornar ao menu durante a execução.

## Estrutura do projeto

```text
.
├── Arkanoid_v1.py       # Versão simples
├── Arkanoid_v2.py       # Versão avançada
├── primeiro_exemplo.py  # Exercício inicial de familiarização com Pygame
└── sons/                # Efeitos sonoros e músicas usados pela versão 2
```

## Uso de inteligência artificial

Este projeto também registra uma etapa importante do processo de aprendizagem: a comparação entre duas formas de desenvolvimento.

- Na **versão 1**, o uso de IA foi menor. A implementação priorizou a compreensão das estruturas básicas e das mecânicas mínimas do Arkanoid.
- Na **versão 2**, a IA foi utilizada com mais frequência como apoio para explorar melhorias, organizar recursos adicionais e alcançar um resultado mais completo.

Em ambas as versões, o código foi analisado, adaptado e executado no projeto. A IA foi utilizada como ferramenta de apoio ao aprendizado, e não como substituta da compreensão da implementação.

## Créditos da atividade

Atividade prática de programação com Python e Pygame, com foco no desenvolvimento das capacidades de experimentação, resolução de problemas e compreensão do código.