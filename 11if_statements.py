# if statemets are used when certains conditions are true
# exaple
# If it's sunny - drink water
# if it's cool - wear warm clothes
# if not both - enjoy the day!

weather = input("How's the weather today(hot/cold/ )? ").lower()

if weather == 'hot':
    # this is block of code ececuted when the above condition is True
    print("Please drink plenty of water! ")
elif weather == 'cold':
    print("Please wear warm clothes! ")
else:
    print("Enjoy the lovely day! ")

# Exercise - credit score
price = 1000000
print("The cost is 1,000,000")
good_credit = False
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Your downpayment is ${down_payment}")
