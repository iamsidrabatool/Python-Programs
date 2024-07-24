#MAP

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))

 # FILTER
#def filter_function(a):
 # return a>2
  
newnewl = list(filter(lambda a:a>2, numbers))
print(newnewl)

#REDUCE

  
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)