# When you wanna store key, value pairs you can do that with the Dictionaries
# name = {key:value}

# Example - think of a scenario where you wanna store details of a customer - name, email, phone
# The keys shouls be different, you can't define 2 keys like age = 10 age = 11 - this is not allowed
customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}

# Accessing the values
print(customer['name'])
# This gives us error
# print(customer['name_'])

print(customer.get("name"))
# This doesn't give us an error
print(customer.get("name_"))

# Getting default values from the dictionary
print(customer.get("birthdate", "Jan 1 1980"))

# Updating the value - changing name to RN Tejas
customer['name'] = "RN Tejas"
print(customer)

# Adding Key, Value Pair!
customer["birthdate"] = "Sep 19 2005"
print(customer)

# Exercise - convert numbers(1,2,3) to string(one, two,three)
numbers = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
}

user_mobile_number = input("Phone: ")
output = ""
for number in user_mobile_number:
    # print(numbers[number])
    output += numbers.get(number, "!") + " "
print(output)
