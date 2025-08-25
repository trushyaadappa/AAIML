import time
import os

grid = [
    ['.', '.', '.', 'T'],
    ['.', 'O', '.', '.'],
    ['.', '.', 'O', '.'],
    ['A', '.', '.', '.']
]

agent_row, agent_col = 3, 0
agent_direction = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_grid():
    for row in grid:
        print(" ".join(row))
    print("-" * 10)

def get_percept_ahead():
    dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][agent_direction]
    nr, nc = agent_row + dr, agent_col + dc

    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        return grid[nr][nc]
    return "WALL"

def simple_reflex_agent_reduced():
    global agent_row, agent_col, agent_direction

    percept = get_percept_ahead()
    print(f"Agent perceives: {percept}")

    if percept in ['O', 'WALL']:
        print("Action: Turn Right")
        agent_direction = (agent_direction + 1) % 4
    elif percept == 'T':
        print("Action: Pick up Task")
        dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][agent_direction]
        grid[agent_row + dr][agent_col + dc] = '.'
    else:
        print("Action: Move Forward")
        grid[agent_row][agent_col] = '.'  
        dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][agent_direction]
        agent_row, agent_col = agent_row + dr, agent_col + dc
        grid[agent_row][agent_col] = 'A'  

print("Initial Grid:")
display_grid()
time.sleep(1)

for step in range(10): 
    clear_screen()
    print(f"Step {step + 1}:")
    simple_reflex_agent_reduced()
    display_grid()
    time.sleep(0.8)
