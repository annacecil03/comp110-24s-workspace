def bar(a: str) -> None:
    print(foo(1, a))

def foo(a: int, b: str) -> int:
    return a + len(b)

bar("Comp") #this is the point of calling the function, this is why bar came come before foo

#getting output of 5 because you are in the frame of foo

