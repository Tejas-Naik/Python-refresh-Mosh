course = "Python for Beginners"

# to get the length of the string we use len() - function
print(len(course))

# string is an object and the functions we can use for the strings are called methods and we can use them after the . in the string 
uppercase_course = course.upper()
lowercase_course = course.lower()
print(uppercase_course)
print(lowercase_course)

# when you apply all these methods on a string the original ones are not gonna change!
print(course)

# if you want to find a character in the string we use the find()-method and it returns the index of the char
finding_p = course.find("P")
print(finding_p)

# if you want to replace some character in the string with the new one the we use replace()-method
replacing_beginners = course.replace("Beginners", "absolute Beginners!!!!")
print(replacing_beginners)



