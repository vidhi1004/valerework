num2 =int(input("Enter the number to check :"))
def primenum(num):
    if num == 1:
        return False
    if num == 2:
        return True    
    if num % 2 == 0:
        return False
    else:
        num1 = int(num**0.5)+1
        for i in range(3,num1,2):
            if num % i == 0:
                return False
        return True
    
    
if(primenum(num2) == True):
    print("The input is prime number")
else:
    print("The input is not a prime number")
    
            
        