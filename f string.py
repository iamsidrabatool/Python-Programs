letter = "Hey my name is {} and I am from {}"
country = "pakistan"
name = "sidra"

print(letter.format(name, country))
print(f"Hey my name is {name} and I am from {country}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
print(
    f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
print(f"{2 * 30}")
