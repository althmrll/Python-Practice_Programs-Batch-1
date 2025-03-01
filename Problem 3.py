#Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

while True:
    one= int(input("Enter 1st number:"))
    two= int (input("Enter 2nd number:"))
    try:
        sum= one + two
        print ("The sum of", one, "and", two, "is", sum,".")

    except ValueError:
        print ("!!INVALID INPUT. PLEASE ENTER A NUMBER!!")