#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Assign global variables
global count
global one

# Program itself
while True:
    try:
        one = 0
        count = 0
        while count!=10:
            print ("Numbers entered:", count)
            number= int(input("Enter number:"))
            one = one + number
            count = count + 1
        else: 
            print ("The sum of the ten numbers are", one)
    
    except ValueError:
        print ("!!INVALID INPUT. PLEASE ENTER A NUMBER!!")