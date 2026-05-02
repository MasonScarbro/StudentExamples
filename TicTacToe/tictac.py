def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("---+---+---")
    print("\n")


def check_winner(board):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]

    for cond in win_conditions:
        a, b, c = cond
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose position (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid range. Choose 1-9.")
            elif board[move] != " ":
                print("Spot already taken.")
            else:
                return move
        except ValueError:
            print("Enter a number.")


def play_game():
    board = [" "] * 9
    current_player = "X"

    print("Tic Tac Toe")
    print("Positions are numbered 1-9 like this:")
    print("""
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

    while True:
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        result = check_winner(board)
        if result:
            print_board(board)
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()