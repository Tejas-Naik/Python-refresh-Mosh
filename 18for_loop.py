# We use for loops to iterate over the items of a collection
for char in "Python":
    print(char)

for char in ["Mosh", "John", "Sarah"]:
    print(char)

# The range function
for i in range(10):
    print(i)

# Exercise
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(total)

# Let's use the cool function to get the total
print(sum(prices))