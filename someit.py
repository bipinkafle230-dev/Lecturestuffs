def calculator():
    # Asking input from user
    num = float(input("Enter the first number: "))
    num1 = float(input("Enter the second number: "))

    # Asking the operation to perform
    operation = input("What is the operation (+,-,*,/,%,^,**): ")

    # Operation with conditional statements:
    if operation == '+':
        result = num + num1
    
    elif operation == '-':
        result = num - num1
    
    elif operation == '*':
        result = num * num1
    
    elif operation == '/':
        if num1 != 0:
            result = num / num1
        else:
            print("Error: Division by zero is not allowed!")
            return
    
    elif operation == "**":
        result = num ** num1
    
    elif operation == '%':
        if num1 != 0:
            result = num % num1
        else:
            print("Error: Modulo by zero is not allowed!")
            return
    
    elif operation == '^':
        result = num ** num1  # ^ is typically bitwise XOR, use ** for exponentiation
    
    else:
        print("Invalid operation. Please try again.")
        return

    # If everything was successful, print the result
    print(f"The result of {num} {operation} {num1} is: {result}")

# Run the calculator
calculator()

