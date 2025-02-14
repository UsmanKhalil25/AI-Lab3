from queue import PriorityQueue

from graph import Graph, Node


def a_star(graph: Graph, start: Node, goal: Node):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    
    g_score = {node: float('inf') for node in graph.adjacency_list}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph.adjacency_list}
    f_score[start] = graph.h(start)

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            return reconstruct_path(came_from, current), g_score[goal]

        for neighbor, cost in graph.get_neighbours(current):
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + graph.h(neighbor)
                open_set.put((f_score[neighbor], neighbor))

    return None, float('inf')

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    path.reverse()
    return path

def main():
    graph = Graph()
    node1 = Node("the")
    node2 = Node("cat")
    node3 = Node("dog")
    node4 = Node("runs")
    node5 = Node("fast")

    graph.add_node(node1, node2, 2, is_directed=False)
    graph.add_node(node1, node3, 3, is_directed=False)
    graph.add_node(node2, node4, 1, is_directed=False)
    graph.add_node(node3, node4, 2, is_directed=False)
    graph.add_node(node4, node5, 2, is_directed=False)

    start_node = node1
    goal_node = node5

    path, total_cost = a_star(graph, start_node, goal_node)
    print(f"Path: {path}")
    print(f"Total Cost: {total_cost}")

if __name__ == "__main__":
    main()