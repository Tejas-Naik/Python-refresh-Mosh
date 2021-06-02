from random import randint

random_number = randint(1, 10)

guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    if guess == random_number:
        print("You win...!")
        break     
    guess_count += 1
else:
    print("Sorry, you failed!")
    