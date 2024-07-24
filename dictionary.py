dic = {
    "sidra": "tree",
    "Spoon": "item"
}
print(dic["sidra"])
# accessing single value
dic2 = {
    1: "sidra",
    2: "dania",
    3: "jia"
}
print(dic2[1])

# accessing dectionary
dic2 = {
    1: "sidra",
    2: "dania",
    3: "jia"
}
print(dic2)

# all keys access
dic2 = {
    1: "sidra",
    2: "dania",
    3: "jia"
}
print(dic2.keys())
# all values
print(dic2.values())
# all items
print(dic2.items())

for key, value in dic2.items():
    print(f"The value corresponding to the key {key} is {value}")
