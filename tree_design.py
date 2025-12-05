"""
Módulo que implementa os padrões Visitor, Composite, Iterator e State para uma árvore de decisão, juntamente com as classes de nó da árvore.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional


class Node(ABC):
    """
    Classe base abstrata que representa um componente na árvore de decisão (Component).
    Define a interface comum para nós de decisão e nós folha.
    """

    @abstractmethod
    def accept_visitor(self, visitor: NodeVisitor) -> None:
        """
        Aceita um visitante (Visitor) para executar operações sobre o nó.

        Args:
            visitor (NodeVisitor): O visitante que processará o nó.
        """
        pass

    def __str__(self) -> str:
        """
        Retorna a representação em string do nó para identificação.
        """
        return self.__class__.__name__


class DecisionNode(Node):
    """
    Representa um nó interno de decisão que pode conter filhos (Composite).
    """

    def __init__(self) -> None:
        """Inicializa um nó de decisão com uma lista vazia de filhos."""
        self.children: List[Node] = []

    def add_child_node(self, node: Node) -> None:
        """
        Adiciona um nó filho à lista de filhos deste nó de decisão.

        Args:
            node (Node): O nó (Decisão ou Folha) a ser adicionado.
        """
        self.children.append(node)

    def accept_visitor(self, visitor: NodeVisitor) -> None:
        """
        Aceita um visitante e delega para o método específico de visitação de nós de decisão.

        Args:
            visitor (NodeVisitor): O visitante.
        """
        visitor.visit_decision(self)


class LeafNode(Node):
    """
    Representa um nó folha que contém um resultado final ou classificação (Leaf).
    Não possui filhos.
    """

    def __init__(self, value: str) -> None:
        """
        Inicializa o nó folha com um valor de classificação.

        Args:
            value (str): O valor ou rótulo da classe associada a esta folha.
        """
        self.value: str = value

    def accept_visitor(self, visitor: NodeVisitor) -> None:
        """
        Aceita um visitante e delega para o método específico de visitação de nós folha.

        Args:
            visitor (NodeVisitor): O visitante.
        """
        visitor.visit_leaf(self)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} -> '{self.value}'"


##########################################################################################


class NodeVisitor(ABC):
    """
    Interface abstrata para os Visitors.
    Define os métodos de visita para cada tipo concreto de nó (DecisionNode e LeafNode).
    """

    @abstractmethod
    def visit_decision(self, node: DecisionNode) -> None:
        """
        Método chamado ao visitar um DecisionNode.

        Args:
            node (DecisionNode): O nó de decisão sendo visitado.
        """
        pass

    @abstractmethod
    def visit_leaf(self, node: LeafNode) -> None:
        """
        Método chamado ao visitar um LeafNode.

        Args:
            node (LeafNode): O nó folha sendo visitado.
        """
        pass


class DepthVisitor(NodeVisitor):
    """
    Visitor concreto que simula o cálculo da profundidade da árvore.
    """

    def visit_decision(self, node: DecisionNode) -> None:
        print(f"DepthVisitor: Calculando profundidade no nó {node}.")
        for child in node.children:
            child.accept_visitor(self)

    def visit_leaf(self, node: LeafNode) -> None:
        print(f"DepthVisitor: Atingiu a base da árvore no nó {node}.")


class CountLeavesVisitor(NodeVisitor):
    """
    Visitor concreto que simula a contagem de nós folha na árvore.
    """

    def visit_decision(self, node: DecisionNode) -> None:
        print(
            f"CountLeavesVisitor: Atravessando {node} para encontrar folhas."
        )
        for child in node.children:
            child.accept_visitor(self)

    def visit_leaf(self, node: LeafNode) -> None:
        print(f"CountLeavesVisitor: Folha encontrada: {node}.")


##########################################################################################


class PreOrderIterator:
    """
    Iterador que percorre a árvore seguindo a estratégia Pré-Ordem (Pre-Order).
    Visita a raiz primeiro, depois os filhos recursivamente.
    """

    def __init__(self, root: Optional[Node]) -> None:
        """
        Inicializa o iterador com o nó raiz.

        Args:
            root (Optional[Node]): O nó raiz da árvore ou subárvore.
        """
        # A pilha armazena os nós a serem visitados.
        self.stack: List[Node] = [root] if root else []

    def __iter__(self) -> PreOrderIterator:
        return self

    def __next__(self) -> Node:
        """
        Retorna o próximo nó na sequência de iteração.

        Returns:
            Node: O próximo nó visitado.

        Raises:
            StopIteration: Quando não há mais nós a visitar.
        """
        if not self.stack:
            raise StopIteration

        node = self.stack.pop()

        # Se for um nó de decisão, adiciona seus filhos à pilha.
        # Adiciona em ordem reversa para que o primeiro filho seja o próximo a ser pego (LIFO).
        if isinstance(node, DecisionNode):
            for child in reversed(node.children):
                self.stack.append(child)

        return node


##########################################################################################


class BuilderState(ABC):
    """
    Interface abstrata para os estados do processo de construção da árvore.
    """

    @abstractmethod
    def execute_construction_phase(self, builder: TreeBuilder) -> None:
        """
        Executa a lógica específica do estado atual e realiza a transição para o próximo estado.

        Args:
            builder (TreeBuilder): O contexto que mantém o estado atual.
        """
        pass


class TreeBuilder:
    """
    Contexto que gerencia o estado atual da construção da árvore.
    Mantém uma referência para o estado atual e delega a execução para ele.
    """

    def __init__(self) -> None:
        self._state: Optional[BuilderState] = None

    def set_state(self, state: BuilderState) -> None:
        """
        Altera o estado atual do construtor.

        Args:
            state (BuilderState): O novo estado a ser definido.
        """
        self._state = state
        print(
            f"TreeBuilder: Transição de Estado -> {state.__class__.__name__}."
        )

    def advance_construction(self) -> None:
        """
        Avança o processo de construção delegando a ação para o estado atual.
        """
        if self._state:
            self._state.execute_construction_phase(self)
        else:
            print("TreeBuilder: Nenhum estado definido para avançar.")


class SplittingState(BuilderState):
    """
    Estado responsável pela divisão dos nós (Splitting).
    Simula a escolha do melhor atributo para dividir os dados.
    """

    def execute_construction_phase(self, builder: TreeBuilder) -> None:
        print(
            "Estado Splitting: Analisando ganho de informação e dividindo nós."
        )
        # Lógica simulada de transição para o próximo estado (Poda)
        builder.set_state(PruningState())


class PruningState(BuilderState):
    """
    Estado responsável pela poda da árvore (Pruning).
    Simula a remoção de ramos irrelevantes para evitar overfitting.
    """

    def execute_construction_phase(self, builder: TreeBuilder) -> None:
        print(
            "Estado Pruning: Avaliando complexidade e podando ramos desnecessários."
        )
        # Lógica simulada de transição para o próximo estado (Parada)
        builder.set_state(StoppingState())


class StoppingState(BuilderState):
    """
    Estado final de parada (Stopping).
    Indica que a construção da árvore foi concluída.
    """

    def execute_construction_phase(self, builder: TreeBuilder) -> None:
        print(
            "Estado Stopping: Critérios de parada atingidos. Construção finalizada."
        )
        # Fim do ciclo, não há mais transições automáticas.
