#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

while True:
    try:
        one= int(input("Enter 1st number:"))
        two= int(input("Enter 2nd number:"))

        if one==two:
            print (one, "and", two, "are equal.")
        else:
            print (one, "and", two, "are NOT equal.")

    except ValueError:
        Print ("!!INVALID INPUT. PLEASE ENTER A NUMBER!!")