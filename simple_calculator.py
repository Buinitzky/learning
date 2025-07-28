#keep the calculator working until the user decides not to
while True:
    #verify the input are numbers
    try:
        first_number = input("Introduce a number: ")
        first_number_float = float(first_number)
    #if inputs are not numbers throw an error
    except ValueError:
        print("Please enter a number.")
        continue

    try:
        second_number = input("Introduce another number: ")
        second_number_float = float(second_number)
    except ValueError:
        print("Please enter a number.")
        continue

    operator = input("Choose an operator (+, -, *, /): ")

    if operator not in ("+", "-", "*", "/"):
        raise ValueError("Invalid operation")
        continue

    if operator == "+":
        print(first_number_float + second_number_float)
    elif operator == "-":
        print(first_number_float - second_number_float)
    elif operator == "*":
        print(first_number_float * second_number_float)
    elif operator == "/":
        if second_number_float == 0:
            print("can't divide by zero")
            continue
        else:
            print(first_number_float / second_number_float)

    continue_working = input("\nDo you want to continue? (y/n): ")
    if continue_working.lower() != "y":
        print("bye")
        break