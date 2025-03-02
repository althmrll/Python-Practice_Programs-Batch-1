#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

while True:
    try:
        one= int(input("Enter 1st number:"))
        two= int(input("Enter 2nd number:"))
        power= one**two
        print (one, "raise to", two, "is", power, ".")
    except ValueError:
        print ("!!INVALID INPUT. PLEASE ENTER A NUMBER!!")