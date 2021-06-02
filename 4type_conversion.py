# Type conversion is the way of converting types of variables
birth_year = input("Birth year: ")
current_year = 2021
# print(current_year - birth_year) # this will give you an error because the input accepts STRING so we have to convert it to integer

# Converting str to int
birth_year = int(birth_year)
print(current_year - birth_year)

# TO get the type of an object we use type()- function
print(type(birth_year))

# Exercise
# Pound to Kilogram
user_weight_in_pounds = int(input("Please enter your weight in pounds: "))
user_weight_in_kg = user_weight_in_pounds * 0.453
print("You are " + str(user_weight_in_kg) + "KG")
