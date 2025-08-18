#ASCII grid

grid = [
    "----T-",
    "-S----",
    "--T-T-"
]

start = None
tasks = []

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == 'S':
            start = (i, j)
        elif cell == 'T':
            tasks.append((i, j))

print("Start:", start)
print("Tasks:", tasks)