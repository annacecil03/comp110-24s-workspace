"""Demonstrate Basic List Syntax"""

#create an empty list
grocery_list: list[str] = list() # <- constructor, same as str()
grocery_list: list[str] = [] # <- literal, same as ""
print("empty list: ")
print(grocery_list)


# add to a list
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding things:")
print(grocery_list)

# create a list with objects in it
grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated list: ")
print(grocery_list2)
print("Add another thing:")
grocery_list2.append("whipped cream")
print(grocery_list2)

# Indexing
print("Printing one item:")
print(grocery_list[2])

# Modifying by Index

x: list[str] = ["c", "a", "r", "s"]
x[2] = "t"
print(x)

grocery_list[0] = "cheerios"
print("Modifying: ")
print(grocery_list)

# Length of a list
print("Length:")
print(len(grocery_list))

#Removing an item
grocery_list.pop(0)
print("Remove an item:")
print(grocery_list)

grocery_list3: list[str] = ["bananas"]
grocery_list3.append("bananas")
print(grocery_list3)

def display(grocery1: list[str]) -> None:
    print(grocery1)

display(grocery_list)
#just printing a list. need [] as hard brackets
# prints none because there is not anything to return or a return type

def create(variable1: str, variable2: str) -> list[str]:
    new_list: list[str] = [variable1, variable2]
    return new_list

x: list[str] = create("Hello", "world")
print(x)

