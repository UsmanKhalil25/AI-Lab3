from node import Node
from frontier import Frontier, FrontierType

MOVES = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, 1),   # Right
    (0, -1)   # Left
]

def is_valid_position(position, rows, columns):
    return (0 <= position[0] < rows) and (0 <= position[1] < columns)

def get_next_position(current_node, move):
    return (current_node.state[0] + move[0], current_node.state[1] + move[1])

def backtrack_solution(node):
    moves = []
    while node.parent:
        moves.append(node.action)
        node = node.parent
    return moves[::-1]  

def find_shortest_path(rows, columns, start, end):
    frontier = Frontier(FrontierType.QUEUE)  
    visited = set()

    start_node = Node(start)
    frontier.add(start_node)
    visited.add(start)

    while frontier:
        current_node = frontier.remove()

        if current_node.state == end:
            print("Path found!")
            return backtrack_solution(current_node)

        for move in MOVES:
            next_position = get_next_position(current_node, move)

            if not is_valid_position(next_position, rows, columns):
                continue

            if next_position not in visited:
                visited.add(next_position)
                new_node = Node(next_position, move, current_node)
                frontier.add(new_node)

    print("No path found.")
    return None

def main():
    rows = 4
    columns = 4

    grid = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]

    start = (0, 0)
    end = (3, 3)

    print("Finding the shortest path using BFS...")
    path = find_shortest_path(rows, columns, start, end)

    if path:
        print("Shortest path:")
        for step, move in enumerate(path, 1):
            print(f"Step {step}: Move {move}")
    else:
        print("No path exists.")

if __name__ == "__main__":
    main()