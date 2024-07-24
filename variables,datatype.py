def calculateGmean(a, b):
    mean = (a+b)/(a*b)
    print(mean)


def isGreater(a, b):
    if (a > b):
        print("A IS GREATER THAN B")
    else:
        print("a is less than b")


a = 8
b = 4
isGreater(a, b)
calculateGmean(a, b)


c = 5
d = 4
isGreater(c, d)

calculateGmean(c, d)
