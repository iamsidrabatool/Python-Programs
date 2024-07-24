a = "!!! sidra!! !!!!!!!!!"
# length
print(len(a))
print(a)
# capital
print(a.upper())

# lower
print(a.lower())

print(a.rstrip("!"))
# replace
print(a.replace("sidra", "janita"))
# list
print(a.split(" "))
# captlilize first word
heading = "introduction"
print(heading.capitalize())

x = "sidra"
print(x.capitalize())
# center
y = "Welcome to my world"
print(len(y))
print(len(y.center(40)))

# count
z = "khan,khan "
print(z.count("khan"))


str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "my name is sidra "
print(str1.find("is"))

# isalnum
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "WelcomeToTheConsole££"
print(str1.isalnum())

#ISALPHA
str1 = "Welcome"
print(str1.isalpha())

# lowercase
str1 = "hello world"
print(str1.islower())

# printable
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())


str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())

str1 = "    "  # using Spacebar
print(str1.isspace())
str2 = "  "  # using Tab
print(str2.isspace())

# title
str1 = "World Health Organization"
print(str1.istitle())

str1 = "World Health Organization"
print(str1.istitle())

#STARTWITH
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

#ENDWITH
str1 = "Python is a Interpreted Language"
print(str1.endswith("Language"))

#SPACEBAR
str1 = "Python is a Interpreted Language"
print(str1.swapcase())
