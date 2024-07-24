for i in range(5):
    print(i)
else:
    print("sorry")

for x in range(6):
    print(x)
    if x == 4:
        break
else:
    print("sorry")


for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of loop")
