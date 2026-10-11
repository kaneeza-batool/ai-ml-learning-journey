name = input("Enter your name")

# Remove whitespaces
name = name.strip()
"""
# how strip function works
input =                       David
output = David
"""

# Capitalize the first letter of string
name = name.capitalize()
"""
# how capitalize function works
input = david malan
output = David malan
"""

# Capitalize the first letter of title...
name = name.title()
"""
# how capitalize function works
input = david malan
output = David Malan
"""

# we can chain multiple functions together
# Remove whitespace from str and capitalize user's name
name = name.strip().title()
name = input("Enter your name").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")
"""
# how split function works
input = david malan
output:
first = David 
last = Malan
"""

