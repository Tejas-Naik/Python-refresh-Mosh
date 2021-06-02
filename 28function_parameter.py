# This is the function we created in the last tutorial but this is not as good as greeting user with their name
# so in this function we take input/'parameter' from the user and we greet them with their name

def greet_user(name:str="John Smith"):   # Taking input named 'name' -> name = input()- type:str, default="John Smith"
    print(f"Hi {name}!")    # Using the input
    print(f"Welcome aboad, {name}!")

greet_user("Jack")         # Providing the parameter which is called arguement
greet_user()
