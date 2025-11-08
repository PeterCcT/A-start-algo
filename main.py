from copy import deepcopy


Maze = list[list[int]]
NodeCoord = tuple[int, int]

MAZE_BEGINNING = 'S'
MAZE_END = 'E'
MAZE_WALL = 1


def print_maze_state(maze: Maze, path: list[NodeCoord]):
    maze_copy = deepcopy(maze)
    for row, row_value in enumerate(maze_copy):
        for col, _ in enumerate(row_value):
            if (row, col) in path:
                maze_copy[row][col] = '*'
        print(row_value)
    print('\n')


def get_maze_beginning_and_end(maze: Maze) -> tuple[NodeCoord, NodeCoord]:
    beginning_coords = None
    end_coords = None
    
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == MAZE_BEGINNING:
                beginning_coords = (row, col)
            if maze[row][col] == MAZE_END:
                end_coords = (row, col)
    
    return beginning_coords, end_coords


def calculate_heuristic(node: NodeCoord, goal: NodeCoord) -> int:
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def get_neighbors(maze: Maze, node: NodeCoord) -> list[NodeCoord]:
    row, col = node
    neighbors = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for direction_row, direction_col in directions:
        new_row = row + direction_row
        new_col = col + direction_col

        if new_row < 0 or new_row >= len(maze):
            continue
        if new_col < 0 or new_col >= len(maze[0]):
            continue

        if maze[new_row][new_col] == MAZE_WALL:
            continue
        
        neighbors.append((new_row, new_col))
    
    return neighbors


def find_shortest_maze_path(maze: Maze):
    start, goal = get_maze_beginning_and_end(maze)
    
    if not start or not goal:
        raise ValueError('Maze should have an start (S) and end (E)')

    real_cost = {start: 0}
    estimated_total_cost = {start: calculate_heuristic(start, goal)}
    came_from = {}

    nodes_to_visit = [start]
    visited_nodes = set()
    
    while nodes_to_visit:
        current = min(nodes_to_visit, key=lambda node: estimated_total_cost.get(node, float('inf')))

        path_so_far = reconstruct_path(came_from, current)
        print_maze_state(maze, path_so_far)

        if current == goal:
            final_path = reconstruct_path(came_from, current)
            print(f'Founded path with {len(final_path)} steps')
            return final_path

        nodes_to_visit.remove(current)
        visited_nodes.add(current)

        for neighbor in get_neighbors(maze, current):
            if neighbor in visited_nodes:
                continue

            tentative_cost = real_cost[current] + 1
            if neighbor not in real_cost or tentative_cost < real_cost[neighbor]:
                came_from[neighbor] = current
                real_cost[neighbor] = tentative_cost
                estimated_total_cost[neighbor] = tentative_cost + calculate_heuristic(neighbor, goal)
                
                if neighbor not in nodes_to_visit:
                    nodes_to_visit.append(neighbor)

    print('No path found')
    return []


def reconstruct_path(came_from: dict[NodeCoord, NodeCoord], current: NodeCoord) -> list[NodeCoord]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path



maze_without_solution = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 'E', 1]
]

maze_with_solution = [
    ['S', 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 'E', 0]
]

if __name__ == '__main__':
    print('=== Maze without solution ===')
    find_shortest_maze_path(maze_without_solution)
    print('\n=== Maze with solution ===')
    find_shortest_maze_path(maze_with_solution)
