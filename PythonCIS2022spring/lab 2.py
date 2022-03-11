#******************************************************************************
# Author:           Manisha Shah and Jolene Lund
# Lab:              Lab 2
# Date:             1/18/2022
# Description:      Example: This program prompts a user for their name,
#                   age, and their birthday to figure out when bday is or if it has passed.
# Input:            String name, Integer age, and Integer Birthday
# Output:           name and upcoming birthday.
# Sources:          Lab 2 specifications. W3Schools, tutoring
#
#                   Team- Manisha Shah and Jolene Lund
# ******************************************************************************
from datetime import date, datetime, timedelta

def main():
    age = 0.0
    name = ""
    strBday = ""

    tDay = datetime.now()

    name = input("Enter your Name: ")
#used datetime function to get upcoming or past birthday.
    age = getAgeValidation()
    strBday = getDateValidation()
    getInfo(name,tDay, strBday)

#used compound operator to get the exact days left for birthday.
#used round and formate to get the numeric value, used concatenated strings.
def getInfo(name,tDay, bDay):
    if tDay.month > bDay.month or (tDay.month == bDay.month and tDay.day > bDay.day):
        currentBirthDay = bDay.replace(year=tDay.year)
        difference = (tDay - currentBirthDay)
        print("Hi ",name,",your birthday has just passed by", difference.days, 'days.')
    elif tDay.day == bDay.day and tDay.month == bDay.month:
        print("Dear,",name," Happy Birthday!")
    else:
        print("Hi ",name,", Your next birthday will be on ", bDay.month, "/", bDay.day, "/2022", sep="")


#used integers that accept numeric value.
def getAgeValidation():
    while True:
        try:
            age = int(input("Please Enter your age: "))
            if age <= 0:
                print("Please enter age greater than zero.")
            else:
                return age
        except:
            print("Invalid age entered. Please enter a number greater than zero.")
#chaining method to calculate the date.

def getDateValidation():
    str = ""
    while True:
        try:
            str = input("Please enter your birthday (MM/DD/2022): ")
            print('\n')
            bDay = datetime.strptime(str, '%m/%d/%Y')
            return bDay
        except:
            print("Invalid Date entered. Please try again.")


main()
