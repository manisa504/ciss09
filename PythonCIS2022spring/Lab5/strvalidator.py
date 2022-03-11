# Validates y/n user input and returns more.
def getMoreItems():
    more = ''
    more = input('Would you like to enter item (y/n)? ')
    more = more.lower()
    while more != 'y' and more != 'n':
        print('Please enter a valid answer (y/n)')
        more = input('Would you like to enter another item (y/n)? ')
        more = more.lower()
    return more

# Validates y/n user input for printSummary. 
def getUserInput():
    user1 = ''
    user1 = input('Would you like a receipt (y/n)? ')
    user1 = user1.lower()
    while user1 != 'y' and user1 != 'n':
        print('Please enter a valid answer (y/n)')
        user1 = input('Would you like a receipt (y/n)? ')
        user1 = user1.lower()
    return user1