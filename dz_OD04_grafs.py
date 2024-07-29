class SimpleGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.nodes[node1].add(node2)
        self.nodes[node2].add(node1)  # Для неориентированного графа

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1].discard(node2)
            self.nodes[node2].discard(node1)

    def get_neighbors(self, node):
        return self.nodes.get(node, set())

    def print_graph(self):
        for node, neighbors in self.nodes.items():
            print(f"{node}: {' '.join(map(str, neighbors))}")

# Пример использования
graph = SimpleGraph()

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(4, 5)

print("Граф после добавления рёбер:")
graph.print_graph()

graph.remove_edge(1, 3)
print("\nГраф после удаления ребра между 1 и 3:")
graph.print_graph()

print("\nСоседи узла 4:")
print(graph.get_neighbors(4))