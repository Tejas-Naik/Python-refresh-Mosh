temperature = 30

# there are mainly 3 coparison operatoes '>', '<', '='
# there are sub 3 coparison operatoes '>=', '<=', '==', '!='

if temperature > 30:
    print("It's a hot day!")
elif temperature < 10:
    print("It's a cold day!")
else:
    print("it's a neutral day!")

# Exercise - if the user naem is > 50 VALID NAME, if < 3 VALID NAME
name = input("Please enter your name! ")
if len(name) > 50:
    print("Please enter a Valid Name not greater than 50!!!!")
elif len(name) < 3:
    print("Your name is incorrect please check that out")
else:
    print("I like your name!")
    
