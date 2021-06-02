weight = int(input("please enter your weight: "))
unit = input("(L)bs or (K)gs? ").lower()

if unit == 'k':
    weight_lbs = weight * 2.20
    print(f"You are {weight_lbs} pounds")
elif unit == 'l':
    weight_kgs = weight * 0.45
    print(f"You are {weight_kgs} pounds")
