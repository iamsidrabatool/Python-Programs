# By default arguent
def average(a=2, b=4):
    print("The average is:", a+b/2)


average(2, 3)
average(b=6)


def name(fname, mname="Jhon", lname="Whatson"):
    print("Hello,", fname, mname, lname)


name("Amy")

'keyword argument'
# order change


def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)


name(mname="Peter", lname="Wesker", fname="Jade")

# required argument
# all values must give


def average(a, b, c):
    print("The average is ", (a + b + c) / 2)


average(2, 3, 4)


# variable legth argument
def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))

    # return argument
    def name(fname, mname, lname):
        return "Hello, " + fname + " " + mname + " " + lname


print(name("James", "Buchanan", "Barnes"))
