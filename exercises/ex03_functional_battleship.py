"""EX03 functional battleship."""


__author__: str = "730464679"


import random


# declaring a function for input guess - promt and return user's row or column guess
def input_guess(grid_size: int, guess: str) -> int:
    """Declaring input guess function."""
    assert guess == "row" or guess == "column"
    player_guess: int = int(input("Guess a " + guess + ": "))
    while player_guess > grid_size or player_guess < 1:
        player_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return player_guess


# declaring a function to give the size of the grid, user row/column guess, and correctness of guess. print game board
def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guess: bool) -> None:
    """Declaring function for grid."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C" 
    row_idx: int = 1
    while row_idx <= grid_size:
        row_string: str = ""
        column_idx: int = 1
        while column_idx <= grid_size:
            if row_idx == row_guess and column_idx == column_guess:
                row_string += RED_BOX if correct_guess is True else WHITE_BOX
            else:
                row_string += BLUE_BOX
            column_idx += 1
        row_idx += 1
        print(row_string)


# declaring a function for correct guess. given secret boat location and user guess, function will return correct or not
def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Declaring function for correct guess."""
    return True if secret_row == row_guess and secret_column == column_guess else False


# implement the main function to pull everything together
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Tying together previous functions to play game."""
    total_guesses: int = 5
    guess_idx: int = 1
    while guess_idx <= total_guesses:
        print(f"=== Turn {guess_idx}/{total_guesses} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        if correct_guess(secret_row, secret_column, row_guess, column_guess):
            print_grid(grid_size, row_guess, column_guess, True)
            print("Hit!") 
            print(f"You won in {guess_idx}/{total_guesses} turns!")
        else:
            print_grid(grid_size, row_guess, column_guess, False)
            print("Miss!")
        guess_idx += 1
    if guess_idx > total_guesses:
        print(f"X/{total_guesses} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))