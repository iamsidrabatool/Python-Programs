
try:

    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])

except:
    print("Some error occurred")


finally:
    print("I am always executed")


def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1

  except:
     print("Some error occurred")
     return 0
  finally:
     print("I am always executed")

x = func1()
print(x)
