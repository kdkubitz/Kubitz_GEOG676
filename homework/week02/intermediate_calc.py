def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Type \'q\' at anytime to stop")

userInput = ''
while userInput != 'q':
    userInput = input("First Number: ")
    if userInput == 'q':
        break
    firstNum = int(userInput)

    userInput = input("Operator: ")
    if userInput == 'q':
        break
    operator = userInput

    userInput = input("Second Number: ")
    if userInput == 'q':
        break
    secondNum = int(userInput)

    if operator == '+':
        print("Result: ", add(firstNum, secondNum))
    elif operator == '-':
        print("Result: ", subtract(firstNum, secondNum))
    elif operator == '*':
        print("Result: ", multiply(firstNum, secondNum))
    elif operator == '/':
        print("Result: ", divide(firstNum, secondNum))
    else:
        print("Invalid operator provided")

