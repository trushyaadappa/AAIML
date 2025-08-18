#tic-tac-toe

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn")
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("Please enter valid integers.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == ' ':
                board[row][col] = current_player
                print_board(board)

                if check_winner(board, current_player):
                    print(f"Player {current_player} wins!")
                    break
                elif is_draw(board):
                    print("It's a draw!")
                    break

                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("That spot is already taken.")
        else:
            print("Invalid position. Please choose row and column between 0 and 2.")

play_game()
