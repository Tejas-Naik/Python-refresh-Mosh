# The link methods are the functions that can be used/acted on the lists (class 'List')
# what we ca do with the list 
#   Add, Remove, Existance(item), replace
numbers = [1, 4, 6, 8, 3, 3, 3]
print(numbers)

# adding item to a list
numbers.append(20)
print(numbers)

numbers.insert(3, 5)    # Adding in middle
print(numbers)

# Removing the items
numbers.remove(5)   # removes the number '5'
print(numbers)
# If you want to clear the list or delete all items from it use clear()
# numbers.clear()

# Pop() removes the last item from the list
numbers.pop()      # it removes 20!
print(numbers)

# Finding an item in a list
print(numbers.index(3))    # It returns the (first) index of the item if it exists
print(50 in numbers)

# Counting/number of items in the list
print(numbers.count(3))     # returns the number of item '3' in the list

# If you want to sort the original list
numbers.sort()      # reverse=True
print(numbers)


# If you want to copy the list
new_numbers = numbers.copy()    # if you change the original list now it is not gonna affect the copied list!!!

# Exercise - remove duplicattes from the list
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)

print(numbers)

