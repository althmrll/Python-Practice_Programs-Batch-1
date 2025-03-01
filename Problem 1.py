#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

while True:
    try:
        one= int(input("Enter 1st number:"))
        two= int(input("Enter 2nd number:"))

        if one>two:
            print (one, "is bigger.")
        elif one<two:
            print(two, "is bigger.")
        else:
            print (one, "and", two, "are equal.")

    except ValueError:
        print ("!!INVALID INPUT. PLEASE TYPE A NUMBER!!")

