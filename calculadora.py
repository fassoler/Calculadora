def show(answer):
    if answer.is_integer():
        print(int(answer))
    else:
        print(answer)
while True:
    word = input("Type anything to continue, 'quit' to exit.")
    if word == "quit":
        break
    try:
        first_number = float(input("What would be the first number?"))
        second_number = float(input("What would be the second number?"))
        operation = input("Which operation you want to do? (add / subtract / divide / multiply / power / remainder)")
    except ValueError:
        print("Please type a number.")
        continue
    if operation == "add" or operation == "+":
        answer = first_number + second_number
        show(answer)
    elif operation == "subtract" or operation == "-":
        answer = first_number - second_number
        show(answer)
    elif operation == "divide" or operation == "/":
        if second_number == 0:
            print("You cannot divide by 0.")
        else:
            answer = first_number / second_number
            show(answer)
    elif operation == "multiply" or operation == "*":
        answer = first_number * second_number
        show(answer)
    elif operation == "power" or operation == "**":
        answer = first_number ** second_number
        show(answer)
    elif operation == "remainder" or operation == "%":
        if second_number == 0:
            print("You cannot remainder with a 0.")
        else:
            answer = first_number % second_number
            show(answer)
    else:
        print("?")