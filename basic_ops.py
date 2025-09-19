def main():
    ''' Main function, asks for numbers and operation type'''
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    operation = input("Enter operation (+, -, *, /, all): ")
    print(f"For inputs {num_1} and {num_2}")
    if operation == "+":
        print("Addition:", addition(num_1, num_2)) 
    elif operation == "-":
        print("Subtraction:", subtraction(num_1, num_2)) 
    elif operation == "*":
        print("Multiplication:", multiplication(num_1, num_2))
    elif operation == "/":
        print("Division:", division(num_1, num_2))
    elif operation == "all":
        print("Addition:", addition(num_1, num_2))
        print("Subtraction:", subtraction(num_1, num_2))
        print("Multiplication:", multiplication(num_1, num_2))
        print("Division:", division(num_1, num_2))
    else:
        restart = input("Invalid Input, restart? (y) or (n): ")
        if restart == "y":
            main()
    restart = input("Thank you for using our program, would you like to restart? (y) or (n): ")
    if restart == "y":
        main()

def addition(num_1, num_2):
    '''Adds numbers together'''
    num_3 = num_1 + num_2
    return num_3

def subtraction(num_1, num_2):
    '''Subtracts numbers'''
    num_3 = num_1 - num_2
    return num_3

def multiplication(num_1, num_2):
    '''Multiplies numbers'''
    num_3 = num_1 * num_2
    return num_3

def division(num_1, num_2):
    '''divides numbers'''
    if num_2 == 0:
        restart = input("Do not divide by Zero! Restart? (y) or (n): ")
        if restart == "y":
            main()
    else:
        num_3 = num_1 / num_2
    return num_3

main()