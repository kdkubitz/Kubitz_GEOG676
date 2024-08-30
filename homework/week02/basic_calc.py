FirstNum = int(input("First number: "))
operator = input("Operator: ")
SecondNum = int(input("Second number: "))

if operator == '+':
    print("Result = ", (FirstNum + SecondNum))
elif operator == '-':
    print("Result = ", (FirstNum - SecondNum))
elif operator == '*':
    print("Result = ", (FirstNum * SecondNum))
elif operator == '/':
    print("Result = ", (FirstNum / SecondNum))
else:
    print("Invalid operator")

