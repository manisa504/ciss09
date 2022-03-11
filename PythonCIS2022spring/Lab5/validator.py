
#Validates user float input for cost.
def getCost():
    amount = 0.0

    while True:
        try:
            amount = float(input("Enter item cost: "))
            if amount < 0:
                print("Entry must be greater than 0.")
            else:
                return amount
        except:
            print("Invalid input.")
            print('Valid entry must be a numeric value greater than 0.')