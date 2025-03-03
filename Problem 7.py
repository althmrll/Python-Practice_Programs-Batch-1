#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Assign global variables
global count
global one

print ("Input 10 numbers and we will tell you the sum of those number")
while True:
    try:
        one = 0
        count = 0
        while count!=10:
            number= int(input("Enter number:"))
            one = one + number
            count = count + 1
        else: 
            print ("The sum of the ten numbers are", one)
    
    except ValueError:
        print ("!!INVALID INPUT. PLEASE ENTER A NUMBER!!")
