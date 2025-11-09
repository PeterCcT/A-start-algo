# Algoritmo A* para Resolução de Labirintos 2D

## Descrição do Projeto

Este projeto implementa o **Algoritmo A*** (A-star) para encontrar o caminho mais curto em labirintos 2D. A implementação é feita em Python puro, sem dependências externas, e demonstra visualmente o processo de busca do algoritmo através da impressão dos estados intermediários do labirinto.

## O Problema

O desafio consiste em encontrar o **menor caminho** entre dois pontos em um labirinto 2D:

- **Ponto inicial**: Marcado com `'S'` (Start)
- **Ponto final**: Marcado com `'E'` (End)
- **Paredes**: Representadas pelo número `1`
- **Caminhos livres**: Representados pelo número `0`

O objetivo é determinar a sequência de movimentos (cima, baixo, esquerda, direita) que leva do ponto inicial ao ponto final, minimizando o número total de passos.

## Configuração e Execução

### Requisitos

- Python 3.9 ou superior

### Como Executar

1. Clone ou baixe este repositório
2. Navegue até o diretório do projeto:
   ```bash
   cd A-start-algo
   ```
3. Execute o arquivo principal:
   ```bash
   python main.py
   ```

O programa executará automaticamente dois exemplos: um labirinto sem solução e um labirinto com solução.

### Criando Seu Próprio Labirinto

Para criar um labirinto personalizado, edite o arquivo `main.py` e adicione uma nova matriz:

```python
meu_labirinto = [
    ['S', 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 'E']
]

find_shortest_maze_path(meu_labirinto)
```