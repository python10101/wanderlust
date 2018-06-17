no1=eval(input("Enter the first number: "))
no2=eval(input("Enter the second number: "))

operation = input('''Please select the desired math operation:\n + for addition \n - for subtraction \n * for multiplication \n / for division\n''')

if operation == '+':
    
        print("Addition is:\n ")
        print("{}+{}= ".format(no1,no2))

elif operation == '-':

        print("Subtraction is:\n ")
        print("{}+{}= ".format(no1,no2))

elif operation == '*':
        
        print("Multiplication is:\n ")
        print("{}*{}= ".format(no1,no2))

elif operation == '/':
    if no2!=0:
        print("Divison is:\n ")
        print("{}/{}= ".format(no1,no2))
    else:
        print("Re-enter a correct number.")        
        
else:
        print("Invalid choice")
        

