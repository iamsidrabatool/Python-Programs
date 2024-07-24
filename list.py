l = [2, 3, 7, 5, 8, "sidra"]
print(l[2:4])
print(l)
print(type(l))
print(l[0])
print(l[1])

# negative indexing
print(l[-3])


if 5 in l:
    print("yes")
else:
    print("no")

# list comprehension
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)
