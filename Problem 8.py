# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers

global odd
global count

print ("Input ten numbers and we will tell you how many are odd.")

while True:
    try:
        count = 0
        odd = 0

        while count != 10:
            number= int(input("Enter number:"))
            count = count + 1
            if number == odd:
                odd= odd+1
        
        else:
            print (odd, "numbers in the list are odd.")

    except ValueError:
        print ("!!INVALID INPUT PLEASE ENTER A NUMBER!!")