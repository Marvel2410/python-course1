num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+ or -): ")

if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
else:
    print("Unknown operator")
