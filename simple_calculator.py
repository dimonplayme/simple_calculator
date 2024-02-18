def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Welcome to my calculator")
print(f"Choose an operation\n")
print("1.Add")
print("2.substract")
print("3.Multiply")
print("4.divide")
while True:
 choice = input("Enter a choice (1/2/3/4) ")
 if choice in ('1' , '2,' , '3' , '4'):
    try :
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
    except ValueError:
        print("Input valid number")
        continue
    if choice == '1':
        print(num1, "+" , num2, "=" , add(num1 , num2))
    elif choice == '2':
        print(num1 , "-" , num2 , "=", substract(num1 , num2))
    elif choice == '3':
        print(num1 , "*" , num2 , "=", multiply(num1 , num2))
    elif choice == '4':
        print(num1 , "/" ,num2 , divide( num1, num2))
        next_calculation = input("Lets do the next calculation(yes/no):")
 if next_calculation == "no":
   break
else:
    print("This is an invalid input")




























