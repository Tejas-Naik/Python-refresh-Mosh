# Tuples are the one of the Data Structures of Python
# Tuples are less in size compared to Lists
# you can't modify the content of the Tuple they are IMMUTABLE
numbers = (1, 2, 3)

# There are only 2 methods you can access on the Tuples - count, index
print(numbers.count(1))
print(numbers.index(2))

# If you try to edit the values of the tuple you will get an error
numbers[0] = 10

