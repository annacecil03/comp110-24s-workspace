"""EX02 battleship part 2 with 4 rows"""

__author__: int = 730464679


grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

guess_row: int = int(input("Guess a row: "))
while guess_row > grid_size or guess_row < 1:
    guess_row = (int(input("The grid is only 4 by 4. Try again: ")))

guess_column: int = int(input("Guess a column: "))
while guess_column > grid_size or guess_column < 1:
    guess_column = (int(input("The grid is only 4 by 4. Try again: ")))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result_box: str = RED_BOX if guess_row == secret_row and guess_column == secret_column else WHITE_BOX

row_idx: int = 1
while row_idx <= grid_size:
    row_string: str = ""
    column_idx: int = 1
   
    if row_idx == guess_row:
        while column_idx <= grid_size:
            if column_idx == guess_column:
                row_string += result_box
            else:
                row_string += BLUE_BOX
            column_idx += 1
    else:
        while column_idx <= grid_size:
            row_string += BLUE_BOX
            column_idx += 1
    
    print(row_string)
    row_idx += 1

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")  
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")

 



