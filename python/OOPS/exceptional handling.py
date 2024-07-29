
'''
exception handling:
Exception handling in Python allows you to manage errors and exceptions gracefully, ensuring that your program can continue running or terminate cleanly when unexpected issues arise. Python uses the try, except, else, and finally blocks to handle exceptions.
'''
try:
    # Code that might cause an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    # This block runs if a ZeroDivisionError occurs
    print("Error: Cannot divide by zero.")
except ValueError:
    # This block runs if a ValueError occurs (e.g., invalid input)
    print("Error: Invalid input. Please enter numeric values.")
else:
    # This block runs if no exceptions occur
    print(f"The result is: {result}")
finally:
    # This block always runs, regardless of whether an exception occurred
    print("Execution completed.")
