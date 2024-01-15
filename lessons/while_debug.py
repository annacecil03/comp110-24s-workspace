"""Practice while loops and debug them"""

my_number: int = 86753089
my_number_str: str = str(86753089)
total: int = 0
index: int = 0
while index < len(my_number_str):
    value: int = int(my_number_str[index])
    total += value  
    index += 1