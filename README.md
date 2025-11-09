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

## Como Funciona o Algoritmo A*

### Conceito Geral

O Algoritmo A* é um algoritmo de busca informada que combina características de busca em largura com uma heurística para encontrar o caminho mais eficiente. Ele é considerado **ótimo** e **completo**, garantindo encontrar o menor caminho quando ele existe.

### Componentes Principais

#### 1. Função de Custo Real (`real_cost`)

Representa o **custo real** do caminho já percorrido do início até cada nó. No nosso caso, é simplesmente o número de passos dados.

```python
real_cost[nó] = número de passos do início até este nó
```

#### 2. Heurística - Distância de Manhattan (`calculate_heuristic`)

A heurística estima o custo restante do nó atual até o objetivo. Usamos a **Distância de Manhattan**, que calcula a soma das diferenças absolutas entre coordenadas:

```python
h(nó) = |linha_nó - linha_objetivo| + |coluna_nó - coluna_objetivo|
```

**Exemplo:**
- Nó atual: (1, 2)
- Objetivo: (4, 5)
- Heurística: |1 - 4| + |2 - 5| = 3 + 3 = 6

Esta heurística é **admissível** (nunca superestima o custo real) e **consistente**, garantindo que o A* encontre a solução ótima.

#### 3. Custo Total Estimado (`estimated_total_cost`)

Combina o custo real com a heurística para priorizar os nós mais promissores:

```python
f(nó) = real_cost[nó] + calculate_heuristic(nó, objetivo)
```

### A Combinação: Custo Real + Heurística de Manhattan

O grande diferencial do A* está na **combinação inteligente** entre o custo do caminho percorrido e a estimativa de distância até o objetivo. Esta união garante a **eficiência** do algoritmo.

#### Como a Combinação Funciona na Prática

**1. Custo Real (`g(nó)`)** - O Passado
- Representa quantos passos **já foram dados** do início até o nó atual
- Garante que o algoritmo considere o esforço já investido
- Exemplo: Se já dei 5 passos para chegar em um nó, `real_cost = 5`

**2. Heurística de Manhattan (`h(nó)`)** - O Futuro
- Estima quantos passos **ainda faltam** até o objetivo
- Fornece uma direção, guiando a busca
- Exemplo: Se estou a 3 linhas e 2 colunas do objetivo, `heurística = 5`

**3. Custo Total (`f(nó) = g(nó) + h(nó)`)** - A Decisão
- Combina passado + futuro para tomar decisões inteligentes
- O algoritmo sempre escolhe o nó com **menor f(nó)**
- Exemplo: `f(nó) = 5 + 5 = 10` (5 passos dados + 5 estimados)

#### Exemplo Prático da Combinação

Imagine dois caminhos possíveis a partir do início 'S':

**Caminho A:**
- Passos dados: 3
- Distância estimada ao objetivo: 8
- **Custo total: 3 + 8 = 11**

**Caminho B:**
- Passos dados: 4
- Distância estimada ao objetivo: 5
- **Custo total: 4 + 5 = 9**

O A* escolhe o **Caminho B** porque, apesar de ter dado mais passos, está mais próximo do objetivo (custo total menor). Esta decisão é possível graças à combinação dos dois fatores.

#### Por Que Esta Combinação Encontra o Menor Caminho?

1. **Evita Caminhos Longos**: O custo real impede que o algoritmo siga caminhos que já consumiram muitos passos desnecessários

2. **Mantém o Foco no Objetivo**: A heurística de Manhattan guia a busca na direção certa, evitando explorar áreas distantes do objetivo

3. **Balanceamento Perfeito**: Ao somar ambos, o algoritmo não é nem muito conservador (só olhando o passado) nem muito otimista (só olhando o futuro)

4. **Admissibilidade**: Como a Distância de Manhattan nunca superestima o custo real, o A* garante encontrar o caminho ótimo

#### Visualização da Combinação no Código

```python
# Para cada vizinho encontrado
tentative_cost = real_cost[current] + 1  # Custo real: passos já dados + 1 passo novo

# Se este caminho for melhor
if neighbor not in real_cost or tentative_cost < real_cost[neighbor]:
    real_cost[neighbor] = tentative_cost  # Atualiza custo real (passado)
    estimated_total_cost[neighbor] = tentative_cost + calculate_heuristic(neighbor, goal)  # Combina com heurística (futuro)
```

A cada iteração, o algoritmo recalcula ambos os componentes e os combina, garantindo que sempre explore primeiro os nós mais promissores para encontrar o menor caminho no labirinto.

### Funcionamento Passo a Passo

1. **Inicialização:**
   - Adiciona o nó inicial à lista de nós a visitar
   - Define o custo real do nó inicial como 0

2. **Loop Principal:**
   - Seleciona o nó com **menor custo total estimado** da lista
   - Se é o objetivo, reconstrói e retorna o caminho
   - Marca o nó como visitado
   - Explora todos os vizinhos (cima, baixo, esquerda, direita)

3. **Para Cada Vizinho:**
   - Ignora se já foi visitado ou é uma parede
   - Calcula o novo custo tentativo (custo atual + 1)
   - Se encontrou um caminho melhor:
     - Atualiza o custo real do vizinho
     - Atualiza o custo total estimado
     - Registra de onde veio
     - Adiciona à lista de nós a visitar

4. **Reconstrução do Caminho:**
   - Usa o dicionário `came_from` para voltar do objetivo até o início
   - Reverte a lista para obter o caminho correto

### Por Que o A* É Eficiente?

- **Busca Direcionada**: A heurística guia a busca em direção ao objetivo
- **Evita Caminhos Subótimos**: Sempre explora primeiro os caminhos mais promissores
- **Memória de Custos**: Não reprocessa nós de forma ineficiente

## Exemplos de Entrada e Saída

### Exemplo 1: Labirinto Sem Solução

**Entrada:**
```python
maze_without_solution = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 'E', 1]
]
```

**Representação Visual:**
```
S  0  |  0  0
0  0  |  0  |
0  |  0  0  0
|  0  0  E  |

Legenda: | = parede (1)
```

**Saída:**
```
=== Testando maze sem solução ===
['*', 0, 1, 0, 0]
[0, 0, 1, 0, 1]
[0, 1, 0, 0, 0]
[1, 0, 0, 'E', 1]

['*', 0, 1, 0, 0]
['*', 0, 1, 0, 1]
[0, 1, 0, 0, 0]
[1, 0, 0, 'E', 1]

['*', '*', 1, 0, 0]
[0, 0, 1, 0, 1]
[0, 1, 0, 0, 0]
[1, 0, 0, 'E', 1]

... (explorando caminhos)

No path found
```

O algoritmo explora todas as possibilidades e conclui que não há caminho possível devido às paredes bloqueando o acesso ao objetivo.

