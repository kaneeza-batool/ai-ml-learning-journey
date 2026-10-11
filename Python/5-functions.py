def main():
    greeting("Kaneeza Batool")
    x = int(input("Enter a value: "))
    print("x squared is", square(x))
    
    
def greeting(name="world"):    # world - default parameter
    print("Hello", name)
    
def square(n):
    return n*n

main()