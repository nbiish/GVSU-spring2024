class IcedCoffeeMachine:
# TODO -- ICED COFFEE MACHINE: #########################################
# [ ] - num of cups remaining in machine is INT
# [ ] - total sales throughout day in cent INT?
# [ ] - customers current credit inserted + price that never changes
#      - example:
#           120 of (180)  
### END OF TODO ########################################################

# INITIALIZE VARIABLES #################################################
    def __init__(self, amount):
        self.credit = 0
        self.total_sales = 0
        self.number_of_cups = amount
        self.price_of_drink = 1.80

### END OF INITIALIZE VARIABLES ########################################

# GET FUNCTIONS ########################################################


    def get_inventory(self):
        print(self.number_of_cups)  

    def get_price(self):
        print(self.get_price)

    def cancel_purchase(self):
        self.credit = 0
        print(self.credit)

    def report_status(self):
        inventory = self.number_of_cups
        sales = self.total_sales
        print(f"Inventory: {inventory}\nTotal Sales: {sales}")

    def insert_coin(self, amount):
        allowed_currencies = [5, 10, 25, 100]
        self.credit = amount
        if amount in allowed_currencies:
            if (self.credit >= 180):
                print(f"Please...\nMake A Selection")
            else:
                print(f"Credit: ${self.credit/100.00:.2f}\nPrice: ${self.price_of_drink:.2f}")

    def restock(self, amount):
        if amount >= 0:
            self.number_of_cups = amount
            print(f"new stock is: {self.number_of_cups}")

# [✅] - WORKS WITH 0 STOCK AND MORE THAN 0 STOCK
    def display_greeting(self):
        if self.number_of_cups == 0:
            print(f"Sorry - machine is out of stock")
        else:
            print(f"Iced Coffee!\nPrice: $1.80")

    def make_selection(self):
        if self.credit >= 180:
            self.number_of_cups - 1
            self.total_sales + 1
            # EXAM SAYS 0 -- i would subtract 180
            self.credit = 0
            print(f"Now dispending...\nYour Iced Coffee")
        else:
            print(f"Credit: ${self.credit/100.00:.2f}")


### END OF GET FUNCTIONS ###############################################

if __name__ == "__main__":
    print(f"*"+"ICM1 TESTS"+"*"*27)
    icm1 = IcedCoffeeMachine(9)
    print(icm1.get_inventory())
    # print(icm1.get_price()) #only prints object right now
    print("*"*36)


    print(f"{icm1.report_status()}")
    print("*"*36)


    print("BEFORE ENOUGH:")
    print(icm1.insert_coin(50))
    print("*"*36)


    print("AFTER ENOUGH:")
    print(icm1.insert_coin(25))
    print("*"*36)


    print(icm1.restock(0))
    print(f"*"*36)

    print(icm1.display_greeting())
    print("*"*36)

    print(icm1.make_selection())
    print(icm1.make_selection())
    print("***"+"END OF ICM1 TEST"+"*"*27)
    print("\n"*3)
    print("*"+"ICM2 TESTS"+"*"*27)
    icm2 = IcedCoffeeMachine(12)


    
