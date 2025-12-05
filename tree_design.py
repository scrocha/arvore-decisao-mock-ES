"""
Módulo que implementa os padrões Visitor, Composite, Iterator e State para uma árvore de decisão, juntamente com as classes de nó da árvore.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional


class Node(ABC):
    @abstractmethod
    def accept_visitor(self, visitor: NodeVisitor) -> None:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class DecisionNode(Node):
    def __init__(self) -> None:
        self.children: List[Node] = []

    def add_child_node(self, node: Node) -> None:
        self.children.append(node)

    def accept_visitor(self, visitor: NodeVisitor) -> None:
        visitor.visit_decision(self)


class LeafNode(Node):
    def __init__(self, value: str) -> None:
        self.value: str = value

    def accept_visitor(self, visitor: NodeVisitor) -> None:
        visitor.visit_leaf(self)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} -> '{self.value}'"


##########################################################################################


class NodeVisitor(ABC):
    @abstractmethod
    def visit_decision(self, node: DecisionNode) -> None:
        pass

    @abstractmethod
    def visit_leaf(self, node: LeafNode) -> None:
        pass


class DepthVisitor(NodeVisitor):
    def visit_decision(self, node: DecisionNode) -> None:
        print(f"DepthVisitor: Calculando profundidade no nó {node}.")
        for child in node.children:
            child.accept_visitor(self)

    def visit_leaf(self, node: LeafNode) -> None:
        print(f"DepthVisitor: Atingiu a base da árvore no nó {node}.")


class CountLeavesVisitor(NodeVisitor):
    def visit_decision(self, node: DecisionNode) -> None:
        print(f"CountLeavesVisitor: Atravessando {node} para encontrar folhas.")
        for child in node.children:
            child.accept_visitor(self)

    def visit_leaf(self, node: LeafNode) -> None:
        print(f"CountLeavesVisitor: Folha encontrada: {node}.")


##########################################################################################


class PreOrderIterator:
    def __init__(self, root: Optional[Node]) -> None:
        # A pilha armazena os nós a serem visitados.
        self.stack: List[Node] = [root] if root else []

    def __iter__(self) -> PreOrderIterator:
        return self

    def __next__(self) -> Node:
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
    @abstractmethod
    def execute_construction_phase(self, builder: TreeBuilder) -> None:
        pass


class TreeBuilder:
    def __init__(self) -> None:
        self._state: Optional[BuilderState] = None

    def set_state(self, state: BuilderState) -> None:
        self._state = state
        print(
            f"TreeBuilder: Transição de Estado -> {state.__class__.__name__}."
        )

    def advance_construction(self) -> None:
        if self._state:
            self._state.execute_construction_phase(self)
        else:
            print("TreeBuilder: Nenhum estado definido para avançar.")


class SplittingState(BuilderState):
    def execute_construction_phase(self, builder: TreeBuilder) -> None:
        print(
            "Estado Splitting: Analisando ganho de informação e dividindo nós."
        )
        # Lógica simulada de transição para o próximo estado (Poda)
        builder.set_state(PruningState())


class PruningState(BuilderState):
    def execute_construction_phase(self, builder: TreeBuilder) -> None:
        print(
            "Estado Pruning: Avaliando complexidade e podando ramos desnecessários."
        )
        # Lógica simulada de transição para o próximo estado (Parada)
        builder.set_state(StoppingState())


class StoppingState(BuilderState):
    def execute_construction_phase(self, builder: TreeBuilder) -> None:
        print(
            "Estado Stopping: Critérios de parada atingidos. Construção finalizada."
        )
        # Fim do ciclo, não há mais transições automáticas.
