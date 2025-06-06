num1 = float(input("Enter number 1 :"))
op = input("Enter opertator :")
num2 = float(input("Enter number 2 :"))

if (op == '+'):
    print("Result is:", num1 + num2)
elif (op == '-'):
    print("Result is:", num1 - num2)
elif (op == '*'):
    print("Result is:", num1 * num2)
elif (op == '/'):
    if num2 != 0:
        print("Result is:", num1 / num2)
    else:
        print("Error.")
elif (op == '%'):
    if num2 != 0:
        print("Result is:", num1 % num2)
    else:
        print("Error.")
else:
    print('invalid opertator')
