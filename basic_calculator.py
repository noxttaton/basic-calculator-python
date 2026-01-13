def basic_calculator():
    print("Welcome to my calculator!")
    print("These are our available options:")
    print("1. Sum (+)")
    print("2. Subtraction (-)")
    print("3. Division (/)")
    print("4. Multiplication (*)")
    print("5. Close calculator")

    while True:
        operation = input("\nSelect one of the shown options:")
        if operation == "5":
            print ("Are you sure? Okay, see you later.")
            break
        if operation not in ["1", "2", "3", "4"]:
            print ("Error. Enter a valid option.")
            continue
    
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("ERROR. Enter a valid value.")
            continue

        if operation == "1":
            result = num1 + num2
            print(f"The result of the sum of the numbers {num1} and {num2} is: {result}")
        elif operation == "2":
            result = num1 - num2
            print(f"The result of the subtraction of the numbers {num1} and {num2} is: {result}")
        elif operation == "3":
            if num2 == 0:
                print("ERROR. You cannot divide by 0.")
            else:
                result = num1 / num2
                print(f"The result of the division of the numbers {num1} and {num2} is: {result}")
        elif operation == "4":
            result = num1 * num2
            print(f"The result of the multiplication of the numbers {num1} and {num2} is: {result}")

if __name__ == "__main__":
    basic_calculator()