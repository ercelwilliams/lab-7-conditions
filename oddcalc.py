number1 = int(input("Enter A number: "))
number2 = int(input("Enter Another number: "))

print("Enter which operation would you like to perform? ")
ch = input("Mul, div, or mod ")

result = 0
if ch == 'mul':
    result = number1 * number2
elif ch == 'div':
    result = number1 / number2
elif ch == 'mod':
    result = number1 % number2


else:
    print("Invalid operation")

print(number1, ch , number2, ":", result)