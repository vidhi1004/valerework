num1 = int(input("Enter number 1 :"))
op = input("Enter opertator :")
num2 = int(input("Enter number 2 :"))

if (op == '+'):
    print("Result is:", num1 + num2)
elif (op == '-'):
    print("Result is:", num1 - num2)
elif (op == '*'):
    print("Result is:", num1 * num2)
elif (op == '/'):
    print("Result is:", num1 / num2)
elif (op == '%'):
    print("Result is:", num1 % num2)
else:
    print('invalid opertator')
