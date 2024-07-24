for i in range(20):
    print("5 X", i , "=", 5*i)

# using break
for i in range(20):

    if (i == 10):
        break
    print("5 X", i, "=", 5*i)

#using continue
for i in range(20):

    if (i == 10):
        print("skip the iteration")
        continue
    print("5 X", i, "=", 5*i)
