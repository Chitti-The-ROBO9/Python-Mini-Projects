def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
     return x * y
def divide(x, y):
    if y==0:
        return "Error! Division by zero."
    return x / y
while True:
    c=(input("Enter the operation (+, -, *, / or q to quit): "))
    if c == 'q':
        print("Exiting the calculator. Goodbye!")
        break 
    print("New Calculation")
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if c == 'q':
        print("Exiting the calculator. Goodbye!")
        break 
    if c=='+':
        print("The addition is:",add(a,b))
    elif c=='-':
        print("The subtraction is:",subtract(a,b))
    elif c=='*':
        print("The multiplication is:",multiply(a,b))
    elif c=='/':
        result = divide(a, b)
        if isinstance(result, str):
            print(result)
        else:
            print("The division is:", result)
    else:
        print("Invalid operation")
    