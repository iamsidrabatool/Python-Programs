# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
print("successfully run")

# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
