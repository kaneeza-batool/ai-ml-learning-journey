# Ask user for their name
name = input("What's your name? ")

# Say hello to the user
print("Hello", name)
print("Hello "+ name)
 
# Comma: two arguments. print joins them itself and puts a space between them by default.
# Plus: the two strings are glued into one string first, exactly as written, and then print gets one argument. 
#       No space is added, so you supply it.

""" Is a 
multiline 
comment """

# f-string
print(f"hello {name}")

# using double quotes inside string's double quotes
print("hello \"friend\"")
