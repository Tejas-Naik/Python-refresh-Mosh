# List is one of the Data Structures of Python.
# List stores items in it .
# The index of the list starts at '0'.
names = ['Angela', 'Tim', 'Mosh', 'Andrei', 'Tejas']
print(names)    

# you can also access individual items from the list using the "Index" remember that index starts at '0'
print(names[4])
print(names[-1])
print(names[1:3])   # it returms a list

# Modifying the value of the item in the List
# Changing 'Tejas' to "RNTejas"
names[-1] = "RN Tejas"
print(names)

# Exercise - find the max number in a list without using max()
numbers = [1,2,3,4,5,6,7,8,9]
print(max(numbers))

maximum_number = 0
for number in numbers:
    if number > maximum_number:
        maximum_number = number
print(maximum_number)
