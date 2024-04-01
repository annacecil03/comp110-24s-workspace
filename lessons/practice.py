def short_words(list_1: list[str]) -> list[str]:
    list_2: list[str] = []
    for elem in list_1:
        if len(elem) < 5:
            list_2.append(elem)
        else:
            print(f"{elem} is too long!")
    return list_2   
    

my_list: list [str ] = ["sun", "cloud", "sky"]
print(short_words(my_list))