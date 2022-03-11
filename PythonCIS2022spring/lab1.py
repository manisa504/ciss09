
#******************************************************
# Author:       Manisha Shah
# Assignment:   Lab1.py
# Date:         01/16/22
# Description:  Modify the code and test the results
# Input:        (What the program asks for, and the data Type)
# Output:       Final cost
# Sources:      Assignment 01 Specifications, Google
# *******************************************************


# Shopping program
# Inputs: float cost, float taxRate, float shipping
# Outputs: float totalPrice

def main():
    # type: () -> object
    """

    :rtype: object
    """
    taxRate = 0.0
    shipping = 0.0
    totalCost = 0.0

    totalCost = getItemCosts()
    taxRate, shipping = getOtherCosts()
    printReceipt(totalCost, taxRate, shipping)

    print("Thank you!")


# getItemCosts() prompts a user for a list of item
# costs and returns the sum
def getItemCosts():
    itemCost = 0.0
    totalCost = 0.0
    n = 0
    y = 0
#added a variable called n to generate a code.
    more = 'y'
#had to remove comma ' ' to run the programme.

    while more == 'y':
        itemCost = float(input("Enter item cost $ "))
        totalCost = totalCost + itemCost
        more = input("Do you have more items (y/n): ")
#instead of upper case C in itemcost has lowercase c.
    return totalCost
#print(totalCost)


# getOtherCosts() prompts a user for the tax rate
# and shipping costs and returns both inputs
def getOtherCosts():
    taxRate = 0.0
    shipping = 0.0

    taxRate = float(input("\nEnter tax rate (i.e. .075 for 7.5%): "))
    shipping = float(input("Enter shipping costs $ "))

    return taxRate, shipping
#swap shipping and taxrate.

# printReceipt() accepts total cost, tax rate, and
# shipping costs and calculates and prints the tax 
# amount, and total cost
def printReceipt(totalCost, taxRate, shipping):
    print("\nSubtotal: $ ", format(totalCost, ".2f"))
    print("Tax: $", format((taxRate), ".2f"))
    print("Shipping: $", format(shipping, ".2f"))
    print("------------------------")
    print("Please pay: $", format(totalCost+ totalCost*taxRate + shipping, ".2f"))
#taxRate multiplied by total coast

main()
