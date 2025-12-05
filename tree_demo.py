from tree_design import (
    TreeBuilder,
    SplittingState,
    DecisionNode,
    LeafNode,
    PreOrderIterator,
    DepthVisitor,
    CountLeavesVisitor,
)


def main():
    print("Demonstração do Padrão State:")
    print()

    # Instancia o construtor da árvore (Contexto do State)
    builder = TreeBuilder()

    # Define o estado inicial como Splitting (Divisão)
    builder.set_state(SplittingState())

    # Executa o processo de construção, que passará por todos os estados automaticamente
    builder.advance_construction()  # Executa Splitting e transita para Pruning
    builder.advance_construction()  # Executa Pruning e transita para Stopping
    builder.advance_construction()  # Executa Stopping (Finaliza)

    print()
    print("#" * 60)
    print()

    print("Demonstração do Padrão Composite:")
    print()

    # Criação da estrutura da árvore (Raiz)
    root = DecisionNode()
    print(f"Nó raiz criado: {root}")

    # Adiciona um nó de decisão e uma folha diretamente na raiz
    child_decision_node = DecisionNode()
    root.add_child_node(child_decision_node)
    print(f"Adicionado nó de decisão filho: {child_decision_node}")

    leaf1 = LeafNode("Folha 1")
    root.add_child_node(leaf1)
    print(f"Adicionada folha filha: {leaf1}")

    # Adiciona duas folhas ao nó de decisão filho (Nível mais profundo)
    leaf2 = LeafNode("Folha 2")
    leaf3 = LeafNode("Folha 3")
    child_decision_node.add_child_node(leaf2)
    child_decision_node.add_child_node(leaf3)
    print(f"Adicionadas folhas {leaf2} e {leaf3} ao nó de decisão filho.")

    print()
    print("#" * 60)
    print()

    print("Demonstração do Padrão Iterator (Navegação Pré-Ordem):")
    print()

    # Instancia o iterador para percorrer a árvore
    iterator = PreOrderIterator(root)

    print("Percorrendo a árvore em pré-ordem (Raiz -> Filhos):")
    for node in iterator:
        print(f"- Visitando: {node}")

    print()
    print("#" * 60)
    print()

    print("Demonstração do Padrão Visitor:")
    print()

    print("Executando DepthVisitor")
    depth_visitor = DepthVisitor()
    root.accept_visitor(depth_visitor)
    print()

    print("Executando CountLeavesVisitor")
    count_visitor = CountLeavesVisitor()
    root.accept_visitor(count_visitor)

    print()
    print("#" * 60)
    print()


if __name__ == "__main__":
    main()
