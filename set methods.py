# set
s1 = {1, 2, 4, 5, 2, 4}

s2 = {7, 8, 2, 9, 0}
# joining two sets
print(s1.union(s2))
# ontersection
print(s1.intersection(s2))

# update set
s1.update(s2)
print(s1, s2)
'''first value update'''

# symmetric difference
s3 = s1.symmetric_difference(s2)
print(s3)

# symmetric difference update
s4 = s1.symmetric_difference_update(s2)
print(s4)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

# disjoint

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# superset
print(s1.issuperset(s2))

# subset
print(s1.issubset(s2))

# add
cities = {"Isb", "Mzd", "karachi"}
cities.add("Lahore")
print(cities)

# remove
cities = {"Isb", "Mzd", "karachi"}
cities.remove("karachi")
print(cities)

# delete
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

# pop
'delete one item'
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# clear
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# if
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
