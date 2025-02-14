class Node:
    def __init__(self, state):
        self.state = state

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)

    def __repr__(self):
        return self.state
    
    def __lt__(self, other):
        return self.state < other.state

class Graph:
    def __init__(self):
        self.adjacency_list: dict[Node, list[tuple[Node, int]]] = {}

    def add_node(self, node: Node, neighbor_node: Node, cost: int = 0, is_directed: bool = True) -> None:
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        self.adjacency_list[node].append((neighbor_node, cost))

        if not is_directed:
            if neighbor_node not in self.adjacency_list:
                self.adjacency_list[neighbor_node] = []
            self.adjacency_list[neighbor_node].append((node, cost))

    def get_neighbours(self, node: Node):
        return self.adjacency_list[node]

    def h(self, node: Node):
        heuristics = {
            "the": 4,
            "cat": 3,
            "dog": 3, 
            "runs": 2, 
            "fast": 1, 
        }
        return heuristics[node.state]

