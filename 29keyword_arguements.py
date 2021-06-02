# Positional Arguements -> these are the arguements provided as they are defined/created in the function
# Keyword Arguements -> These are useful in conditions where you wanna use the parameters in different order
# When you wanna call "John Smith" when a user provides smith John

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print(f"Welcome aboard, {first_name} {last_name}!")

# Positional arguements -> "Tejas" is at position 1, "Naik" is at position 2
greet_user("Tejas", "Naik")

# Keyword Arguements -> they are defined with their names
greet_user(first_name="Tejas", last_name="Naik")
print("Keyword arguements in use")
greet_user(last_name="Naik", first_name="Tejas")



