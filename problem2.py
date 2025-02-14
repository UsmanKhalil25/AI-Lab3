from node import Node
import copy
from frontier import Frontier, FrontierType

MOVES = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, 1),   # Right
    (0, -1)   # Left
]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def get_new_position(current_position, move):
    return (current_position[0] + move[0], current_position[1] + move[1])

def is_valid_position(position, rows=3, columns=3):
    return (0 <= position[0] < rows) and (0 <= position[1] < columns)

def find_empty_tile_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None

def get_valid_moves(state):
    empty_tile_position = find_empty_tile_position(state)
    valid_moves = []
    for move in MOVES:
        new_position = get_new_position(empty_tile_position, move)
        if is_valid_position(new_position):
            valid_moves.append(move)
    return valid_moves

def apply_move(state, move):
    empty_tile_position = find_empty_tile_position(state)
    new_position = get_new_position(empty_tile_position, move)
    
    new_state = copy.deepcopy(state)
    new_state[empty_tile_position[0]][empty_tile_position[1]] = state[new_position[0]][new_position[1]]
    new_state[new_position[0]][new_position[1]] = 0
    
    return new_state

def backtrack_solution(node):
    moves = []
    while node.parent:
        moves.append(node.action)
        node = node.parent
    return moves[::-1]  

def run_dfs(start_state, goal_state):
    frontier = Frontier(FrontierType.STACK)
    visited = set()

    start_node = Node(start_state)
    frontier.add(start_node)
    visited.add(tuple(map(tuple, start_state)))

    while frontier:
        current_node = frontier.remove()

        print("Current State:")
        print_matrix(current_node.state)

        if current_node.state == goal_state:
            print("Solution Found!")
            return backtrack_solution(current_node)

        for move in get_valid_moves(current_node.state):
            new_state = apply_move(current_node.state, move)
            state_tuple = tuple(map(tuple, new_state))

            if state_tuple not in visited:
                visited.add(state_tuple)
                new_node = Node(new_state, move, current_node)
                frontier.add(new_node)

    print("No solution found.")
    return None

def main():
    start_state = [
        [1, 2, 5],
        [3, 0, 4],
        [6, 7, 8]
    ]

    goal_state = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    print("Starting DFS to solve the 8-puzzle...")
    solution_path = run_dfs(start_state, goal_state)

    if solution_path:
        print("Solution Path:")
        for step, move in enumerate(solution_path, 1):
            print(f"Step {step}: Move {move}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()