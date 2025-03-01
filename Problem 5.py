# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

while True:
    try:
        one= float(input("Enter 1st number:"))
        two= float(input("Enter 2nd number:"))
        quotient= one/two
        print ("the quotient of", one, "and", two, "is", quotient, ".")
    except ValueError:
        print ("!!INVALID INPUT. PLEASE ENTER A NUMBER!!")