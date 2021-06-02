# Nested loops will be helpful in cases where you want to use 
# (0)(0) 
# (0)(1) 
# (0)(2) 
# (1)(0) 
# (1)(1) 
# (1)(2) 

# for the above code we will use nested for loop
for x_cor in range(0,3):
    for y_cor in range(0, 3):
        print(x_cor, y_cor)

# You can also create Tables using nested for loop
for i in range(1, 11):
    for j in range(1, 11):      # inner/nested loops
        print(f"{i} * {j} = {i*j}")

f_shape = [2, 2, 2, 2, 7]

for num in f_shape:
    output = ""
    for _ in range(num):
        output += "X"
    print(output)
