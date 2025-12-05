# Árvore de Decisão Mock - Engenharia de Software

- Autor: Sillas Rocha da Costa

## Sobre o Projeto

Este projeto consiste em uma implementação mockada (simulada) de uma **Árvore de Decisão**, desenvolvida para demonstrar a aplicação prática de quatro padrões de projeto fundamentais (GoF): **Composite**, **Visitor**, **Iterator** e **State**.

O objetivo principal não é implementar o algoritmo matemático real de aprendizado de máquina, mas sim modelar a arquitetura, a estrutura de classes e os comportamentos do sistema utilizando boas práticas de design de software, type hinting e documentação clara.

## Padrões de Projeto Utilizados

A solução foi arquitetada em torno dos seguintes padrões:

### 1. Composite
Utilizado para representar a estrutura hierárquica da árvore, permitindo tratar nós individuais e composições de nós de maneira uniforme.
- **Component (`Node`)**: Classe base abstrata que define a interface comum.
- **Composite (`DecisionNode`)**: Nós internos que contêm uma lista de filhos.
- **Leaf (`LeafNode`)**: Nós finais que representam o resultado de uma classificação (sem filhos).

### 2. Visitor
Utilizado para separar os algoritmos da estrutura de dados. Isso permite adicionar novas operações à árvore (como contar folhas ou calcular profundidade) sem modificar as classes dos nós.
- **`NodeVisitor`**: Interface para os visitantes.
- **`DepthVisitor`**: Simula o cálculo da profundidade da árvore.
- **`CountLeavesVisitor`**: Percorre a árvore contabilizando o número de nós folha.

### 3. Iterator
Utilizado para fornecer uma maneira de acessar os elementos da árvore sequencialmente sem expor sua representação subjacente.
- **`PreOrderIterator`**: Implementa a travessia em **pré-ordem** (visita a raiz, depois os filhos recursivamente), utilizando uma pilha para gerenciar a navegação de forma iterativa.

### 4. State
Utilizado para gerenciar o ciclo de vida e os comportamentos do processo de construção da árvore.
- **Contexto (`TreeBuilder`)**: Mantém a referência para o estado atual.
- **Estados Concretos**:
    - `SplittingState`: Simula a fase de divisão dos nós (cálculo de ganho de informação).
    - `PruningState`: Simula a fase de poda para otimização e prevenção de overfitting.
    - `StoppingState`: Representa o estado final onde a construção é encerrada.

## Estrutura dos Arquivos

O projeto é composto por dois arquivos principais:

- **`tree_design.py`**: Contém a definição de todas as classes, interfaces e lógica dos padrões de projeto. O código é fortemente tipado e documentado.
- **`tree_demo.py`**: Script principal que importa as classes de `tree_design.py` e executa uma demonstração completa, imprimindo no console o fluxo de execução de cada padrão.

## Pré-requisitos

- Python 3.8 ou superior.
- Nenhuma biblioteca externa é necessária (apenas biblioteca padrão).

## Como Executar

1. Clone o repositório ou baixe os arquivos para sua máquina local.
2. Abra o terminal na pasta do projeto.
3. Execute o script de demonstração:

```bash
python tree_demo.py
```

## Exemplo de Saída

Ao executar o comando acima, você verá logs detalhados demonstrando cada etapa:

```text
Demonstração do Padrão State:

TreeBuilder: Transição de Estado -> SplittingState.
Estado Splitting: Analisando ganho de informação e dividindo nós.
TreeBuilder: Transição de Estado -> PruningState.
Estado Pruning: Avaliando complexidade e podando ramos desnecessários.
TreeBuilder: Transição de Estado -> StoppingState.
Estado Stopping: Critérios de parada atingidos. Construção finalizada.

############################################################

Demonstração do Padrão Composite:

Nó raiz criado: DecisionNode
Adicionado nó de decisão filho: DecisionNode
Adicionada folha filha: LeafNode -> 'Folha 1'
Adicionadas folhas LeafNode -> 'Folha 2' e LeafNode -> 'Folha 3' ao nó de decisão filho.

############################################################

Demonstração do Padrão Iterator (Navegação Pré-Ordem):

Percorrendo a árvore em pré-ordem (Raiz -> Filhos):
- Visitando: DecisionNode
- Visitando: DecisionNode
- Visitando: LeafNode -> 'Folha 2'
- Visitando: LeafNode -> 'Folha 3'
- Visitando: LeafNode -> 'Folha 1'

############################################################

Demonstração do Padrão Visitor:

Executando DepthVisitor
DepthVisitor: Calculando profundidade no nó DecisionNode.
DepthVisitor: Calculando profundidade no nó DecisionNode.
DepthVisitor: Atingiu a base da árvore no nó LeafNode -> 'Folha 2'.
DepthVisitor: Atingiu a base da árvore no nó LeafNode -> 'Folha 3'.
DepthVisitor: Atingiu a base da árvore no nó LeafNode -> 'Folha 1'.

Executando CountLeavesVisitor
CountLeavesVisitor: Atravessando DecisionNode para encontrar folhas.
CountLeavesVisitor: Atravessando DecisionNode para encontrar folhas.
CountLeavesVisitor: Folha encontrada: LeafNode -> 'Folha 2'.
CountLeavesVisitor: Folha encontrada: LeafNode -> 'Folha 3'.
CountLeavesVisitor: Folha encontrada: LeafNode -> 'Folha 1'.

############################################################
```