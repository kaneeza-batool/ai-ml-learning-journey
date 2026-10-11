x = 10
y = 14
# z = x+y

print(x+y)  # 24
print(x-y)  # -4
print(x*y)  # 140
print(x/y)  # 0.7142857142857143
print(x%y)  # 10

a = input("Enter value 1 ")
b = input("Enter value 2 ")
print(a+b)
"""
a = 10
b = 14
output = 1014 instead of 24
# because input always takes input in string and 
+ performs concatenation here 
"""

# correct form
a = int(input("Enter value 1 "))
b = int(input("Enter value 2 "))
print(a+b)

# float datatype
a = float(input("Enter value 1 "))
b = float(input("Enter value 2 "))
c = a + b   # c will be float
c = int(a) + int(b)  # c will be int 
c = int(a+b)

# round method - round(digit, number of precision)
c = round(a+b, 5)

z = 1000
# we want to format as 1,000
print(f"{z:,}")


