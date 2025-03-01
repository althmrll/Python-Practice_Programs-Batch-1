#Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.

whiel True:
one= int(input("Enter 1st number:"))
two= int(input("Enter 2nd numbner:"))

try:
    product = one * two
    print ("The product of", one, "and", two, "is", product,".")
    
except ValueError:
    print ("!!INVALID INPUT. PLEASE ENTER A NUMBER")