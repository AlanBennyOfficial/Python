def print_board(board):
    """Prints the current game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    """Checks if the current player has won."""
    # Check rows for win
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns for win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals for win
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    # Create an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    total_moves = 0

    while total_moves < 9:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (row and column, e.g., 1 1 for top-left): ")

        try:
            row, col = map(int, move.split())
            # Adjust for 0-based index
            row, col = row - 1, col - 1
            # Validate move is within the board and the cell is empty.
            if row not in range(3) or col not in range(3):
                print("Row and column must be between 1 and 3. Try again.\n")
                continue
            if board[row][col] != " ":
                print("That cell is already taken. Try again.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.\n")
            continue

        # Make the move
        board[row][col] = current_player
        total_moves += 1

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        # Switch player: if current is X, next is O, and vice versa.
        current_player = "O" if current_player == "X" else "X"

    # If we exit the loop without a win, it's a tie.
    print_board(board)
    print("It's a tie!")


if __name__ == "__main__":
    tic_tac_toe()
