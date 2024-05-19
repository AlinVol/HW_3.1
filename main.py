number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
action = input("Enter the action (+, -, *, /): ")
if action == '+':
            result = number1 + number2
elif action == '-':
            result = number1 - number2
elif action == '*':
            result = number1 * number2
elif action == '/':
   if number2 != 0:
       result = number1 / number2
   else:
       result = "Error: Division by zero!"
else:
    result = "Error: Invalid action!"
print("Result:", result)