# Functions are useful in repeated work and it also supports DRY-don't repeat yourself
# Example - if you want to greet user Hello, There\n Welcome Abroad
print("Hi there!")
print("Welcome abroad!")

# if you wanna print the above code 3 more times you have to write more 6 lines of code
# But with functions you can do that with only 3 words😱

# def fuction_name:
#     block of code

def greet_user():
    print("Hi there!")
    print("Welcome abroad!")

# After we creted the function now we can call it anywhere we want
greet_user()
greet_user()

