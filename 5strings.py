# If you want to have an uphostrophe in the str you use "" in the outside
course = "Python's course for Beginners"
print(course)

# If you want to have "" in the sentence we use '' in the outside
course = 'Python for "Beginners!"'
print(course)

# if you want to type a big string like the message in the email we use """ message """
message = """OK what does he say about the current state?

        [Mentor] Koose — Today at 10:27 AM
        great

        Tejas Naik — Today at 10:27 AM
        OK Cool
        what are u working on now?

        [Mentor] Koose — Today at 10:28 AM
        flask
        but taking a break now
        i was working on some Ui stuffs

        Tejas Naik — Today at 10:28 AM
        OK Great
        Adobe?

        [Mentor] Koose — Today at 10:29 AM
        yh and UI Briefs

        Tejas Naik — Today at 10:29 AM
        you are doing a lot of things bro!!
        [Mentor] Koose — Today at 10:34 AM
        doing what i can'
        Tejas Naik — Today at 10:36 AM
        ALL The best You can do everything you want!

        Tejas Naik — Today at 2:26 PM
        I want to discuss about the slideshow images on the index page of MOBILE view
        Tejas Naik — Today at 4:41 PM
        Hello"""
print(message)

# getting the characters from the string we use the [] and we provide the index in that 
# The index starts with 0 in Python
course = 'Python for Beginners'
letter_p = course[0]
letter_last = course[-1]
print(letter_p)
print(letter_last)

# To get the series of letters from the string we use the [start:end]
# the indexig works as upto but not including so that it won't take the last letter 
chars_python = course[0:6]  # remember that indexing start from 0
print(chars_python)
