x=4
print(x)

def hello():
    x=5
    print(f"local x is{x}")
    print("hello sidra!")
print(f"global x is{x}")
hello()
print(f"global x is{x}")

x=4
print(x)

#global x change
def hello():
    global x
    x=5
    print(f"local x is{x}")
    print("hello sidra!")
print(f"global x is{x}")
hello()
print(f"global x is{x}")