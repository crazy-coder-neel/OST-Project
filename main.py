def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board, player):
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]

    return [player, player, player] in win_conditions


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for _ in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0,1,2): "))
            col = int(input("Enter col (0,1,2): "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Position out of range! Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

tic_tac_toe()
