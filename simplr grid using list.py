#simple grid using list

def print_grid():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    fill_char = input("Enter the fill character (default is '-'): ")

    if not fill_char:
        fill_char = '-'

    grid = [[fill_char for _ in range(cols)] for _ in range(rows)]
    for row in grid:
        print(' '.join(row))

print_grid()
