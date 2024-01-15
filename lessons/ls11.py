name: str = input("what is your name? ")
if len(name) > 6:
    print("do you have a nickname? ")
elif name == "alyssa":
    print("you must love comp 110!")
else:
    print("nice to meet you, " + name)
    