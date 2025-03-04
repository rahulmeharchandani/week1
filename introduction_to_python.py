def user_info():
    name=input("Enter a name = ")
    age=input("Enter age = ")
    city=input("enter city = ")
    print(f"\nHello {name}, you are {age} years old and live in {city}.\n")

def calculator():
    print("\n Simple Calculator")
    print("Select an operator :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=input("Enter an operation (1/2/3/4) : ")
    num1=float(input("Enter the first number = "))
    num2=float(input("Enter the second number = "))
    if choice=='1':
        result=num1+num2
        print(f"The addition of {num1} and {num2} is {result}")
    elif choice=='2':
        result=num1-num2
        print(f"The subtraction of {num1} and {num2} is {result}")
    elif choice=='3':
        result=num1*num2
        print(f"The multiplication of {num1} and {num2} is {result}")
    elif choice=='4':
        result=num1/num2
        print(f"The division of {num1} and {num2} is {result}")
    else:
        print("invalid operator")


user_info()
calculator()
    