from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional


class Node(ABC):
    @abstractmethod
    def accept_visitor(self, visitor: NodeVisitor) -> None:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class NodeVisitor(ABC):
    @abstractmethod
    def visit_decision(self, node: DecisionNode) -> None:
        pass

    @abstractmethod
    def visit_leaf(self, node: LeafNode) -> None:
        pass


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


class DepthVisitor(NodeVisitor):
    def visit_decision(self, node: DecisionNode) -> None:
        print(
            f"DepthVisitor: Calculando profundidade no nó {node}"
        )
        for child in node.children:
            child.accept_visitor(self)

    def visit_leaf(self, node: LeafNode) -> None:
        print(
            f"DepthVisitor: Atingiu a base da árvore no nó {node}"
        )


class CountLeavesVisitor(NodeVisitor):
    def visit_decision(self, node: DecisionNode) -> None:
        print(
            f"CountLeavesVisitor: Atravessando {node} para encontrar folhas"
        )
        for child in node.children:
            child.accept_visitor(self)

    def visit_leaf(self, node: LeafNode) -> None:
        print(f"CountLeavesVisitor: Folha encontrada: {node}.")
