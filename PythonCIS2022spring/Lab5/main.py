#******************************************************************************
# Author:           Manisha Shah and Jolene Lund
# Lab:              Lab 5
# Date:             2/10/2022
# Description:      This program prompts a user for
#                   items and cost. Then print receipt including shipping. 
# Input:            String item and Float cost
# Output:           display summary/ receipt 
# Sources:          Lab 5 specifications. W3Schools, tutoring
#
#                   Team- Manisha Shah and Jolene Lund
# ******************************************************************************
import validator as v
import strvalidator as sv

#constant declaring only 100 items allowed in list
MAX = 100

def main(): 
  # variables are:
    cost = [0.0] * MAX
    totalCost = 0.0
    grandTotal = 0.0
    item = [''] * MAX
    shipping = 5
    freeShip = 25
    more = 'y'
    trackList = 0
    user1 = ''
   
  # display Welcome message
    print("Welcome to the Budget Store.")

    #while statement will ask user to add more items from the list
    while more == "y":
      item[trackList] = getItem()
      cost[trackList] = getCost()
      totalCost = totalCost + cost[trackList]
      grandTotal = getFinalCost(totalCost, shipping, freeShip)
      more = getMoreItems()
      trackList = trackList + 1

#This will ask user if they want receipt or not. If yes, if statement will call printSummary function to cycle through list and print list content.
    user1 = sv.getUserInput()
    if user1 != 'y':
      print("Thank you for shopping")
    else:
      printSummary(item, cost, trackList, grandTotal)
        

#this will ask users if they would like to enter more items. If so , while loop in main will continue.
def getMoreItems():
  more = sv.getMoreItems()
  return more
 
#This funstion will store items in a list.
def getItem():
  name = ''
  name = input("Please enter the name of your item: ")
  return name
#This function will store cost in a list calling on validation from validator py file.
def getCost():
  cost = v.getCost()
  return cost
 
#This will add or nullify shipping cost if the merchandise is less than $25.  
def getFinalCost(total, shipping, free):
  grandTotal = 0.0
  if total < free:
    grandTotal = total + shipping
    return grandTotal
  else: 
    grandTotal = total
    return grandTotal

    
#This will print a receipt if the user wants one. A while loop is used to access contect of item list and cost list.
def printSummary(item, cost, track, grandTotal):
  counter = 0
  print('\n', 'List of items               cost', sep = '')
  print("***************             ********")

  while counter < track:
    print(item[counter],"                " ,"\t\t", "${:,.2f}".
    format(cost[counter], ".2f"))
    counter = counter + 1

  
  print('************************************')
  print('Please pay',"${:,.2f}".format(grandTotal))


main()