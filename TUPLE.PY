tup = (2, 5, 8, 9, "sidra")
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])

if 5 in tup:
    print("yes")
else:
    print("no")

# tuple slicing
tup2 = tup[0:3]
print(tup2)
