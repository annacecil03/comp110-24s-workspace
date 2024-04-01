"""The file where I import stuff."""

#from lessons import my_functions
from lessons.my_functions import add, my_variable #now add exists instead of adding entire module
from lessons.my_functions import my_variable #same as above

#getting from my functions
#python is going to run the other module INCLUDING print statements
#__name__ == "__main__" #give imported module a name always

print(my_functions.add(4,5))

print(my_functions.my_variable)
