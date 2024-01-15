"""EX01 - Simple Battleship - A step toward Battleship."""

__author__ = "730464679"

player_1_location: str = input("Pick a secret boat location between 1 and 4: ")
if player_1_location < "1":
    print("Error! " + player_1_location + " too low!")
    if player_1_location < "1":
        exit()
if player_1_location > "4":
    print("Error! " + player_1_location + " too high!")
    if player_1_location > "4":
        exit()
player_2_location: str = input("Guess a number between 1 and 4: ")
if player_2_location < "1":
    print("Error! " + player_2_location + " too low!")
    if player_2_location < "1":
        exit()
if player_2_location > "4":
    print("Error! " + player_2_location + " too high!")
    if player_2_location > "4":
        exit()
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
ship_location: str = (BLUE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
       

if player_2_location == player_1_location:
    if player_2_location == "1":
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if player_2_location == "2":
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    if player_2_location == "3":
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    if player_2_location == "4":
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
else:
    if player_2_location == "1":
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if player_2_location == "2":
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
    if player_2_location == "3":
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
    if player_2_location == "4":
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)

if player_1_location == player_2_location:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")