"""Functions that either mutate a list or don't."""

def remove_first(input_list:list[str]) -> None:
    """Remove first element of input_list."""
    #mutates its input
    input_list.pop(0)

def get_first(input_list:list[str]) -> str:
    """Return first element of input_list without mutating."""
    #only calling get_first and returning the first element
    return input_list[0]

def get_and_remove_first(input_list: list[str]) -> str:
    """Removes first element of input_list AND returns it."""
    #pop element will remove and return but there is a simplier way
    elem: str = input_list[0] #accessing first element
    input_list.pop(0) #removing first element
    return elem #returning the element we removed, have to account for the elem before removing because index will change
