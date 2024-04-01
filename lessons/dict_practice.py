"""Practice with dictionaries."""

#syntax for defining a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#remove - dict name.pop(key)
#remove - ice_cream.pop("mint")
ice_cream.pop("mint")
print("After removing mint: ")
print(ice_cream)

#accessing
print(f"Number of vanilla orders: {ice_cream["vanilla"]}")

#updating value
ice_cream["vanilla"] += 1 #relative reassignment operator
print("after adding 1 vanilla:")
print(ice_cream)

#check length of dictionary
len(ice_cream)

#check if key in dictionary, return bool
print("chocolate" in ice_cream)