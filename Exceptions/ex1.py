#demonstrating how to handle a division by zero exception
while True:
    #attempt to convert and divide values
    try:
        number1 = int(input("Enter numerator: "))
        number2 = int(input("Enter denuminator: "))
        result = number1 / number2
    except ValueError: #Tried to convert non-numeric value to integer
        print("You must enter two integers\n")
    except ZeroDivisionError: #denominator was zero
        print("Attempted to divide by zero\n")
    else:
        print(f"{number1:.3f}/{number2:.3f} = {result:.3f}")
        break #If no exceptions occur print the numerater/denominator and the result and terminate the program
