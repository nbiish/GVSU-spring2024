

class LotteryTicket:

    def __init__(self, info):
        # BUILDING OUT OBJECT FROM INPUT DATA TXT FILE
        # EXAMPLE DATA: 
        # Amy, Zu, AnyCity, NC, 27834, 4/20/1960, 5, 12, 37, 39, 68, 11
        
        # Split the info string into multiple pieces separated by ‘,’ or ‘/’
        # Split the input string into tokens using comma as separator
        tokens = info.split(",")
        
        # Extract and clean up the first and last name from the tokens
        self.first = tokens[0].strip()
        self.last = tokens[1].strip()

        # Extract and clean up the city, state, and zip code from the tokens
        self.city = tokens[2].strip()
        self.state = tokens[3].strip()
        self.zip = tokens[4].strip()

        # Extract and clean up the birthday from the tokens
        birthday = tokens[5].strip()
        
        # Split the birthday into day, month, and year using slash as separator
        pieces = birthday.split("/")
        
        # Convert the day, month, and year to integers
        self.day = int(pieces[1])
        self.month = int(pieces[0])
        self.year = int(pieces[2])

        # Format the birth date in the format "year-month-day"
        self.birth_date = f"{self.year}-{self.month}-{self.day}"


        # Extract and clean up the six ticket numbers from the tokens
        self.num1 = int(tokens[6].strip())
        self.num2 = int(tokens[7].strip())
        self.num3 = int(tokens[8].strip())
        self.num4 = int(tokens[9].strip())
        self.num5 = int(tokens[10].strip())
        # Extract and clean up the mega ball number from the tokens
        self.mega_ball = int(tokens[11].strip())

        # Create a list of the ticket numbers
        self.nums = [int(num) for num in tokens[6:11]]
        # Initialize the prize amount to 0.0
        self.prize = 0.0



    # Method to get the first name
    def get_first(self):
        return self.first

    # Method to get the last name
    def get_last(self):
        return self.last

    # Method to get the city
    def get_city(self):
        return self.city

    # Method to get the state
    def get_state(self):
        return self.state

    # Method to get the zip code
    def get_zipcode(self):
        return self.zip

    # Method to get the birth date
    def get_birth_date(self):
        return self.birth_date
    
    # Method to get the birth date
    def get_birth_date(self):
        return self.birth_date
    
    # Method to get the oldest player by comparing the birth dates of the tickets
    def get_oldest_player(self):
        return min(self.tickets, key=lambda ticket: ticket.get_birth_date())


    # Method to get the day of birth
    def get_day(self):
        return self.day

    # Method to get the month of birth
    def get_month(self):
        return self.month

    # Method to get the year of birth
    def get_year(self):
        return self.year

    def get_nums(self):
        return [self.num1, self.num2, self.num3, self.num4, self.num5]

    def get_mega_ball(self):
        return self.mega_ball

    def has_ball(self, val):
        return val in self.get_nums()

    def has_mega_ball(self, val):
        return val == self.get_mega_ball()

    def get_prize(self):
        return self.prize
    
    def set_prize(self, prize):
        self.prize = prize

    def __str__(self):
        return f"{self.get_first()} {self.get_last()}\n{self.get_city()}, {self.get_state()} {self.get_zipcode()}\n{self.get_nums()}   {self.get_mega_ball()}\nPrize: ${self.get_prize()}"


if __name__ == '__main__':
    t = LotteryTicket("Louis,Laker,Allendale,MI,49401,4/20/1985,5,10,15,20,25,7")
    print(t)
    print(t.has_ball(10))
    print(t.has_mega_ball(7))
    print(t.get_nums())
    print(t.get_mega_ball())
    t.set_prize(1000000)
    print(t.prize)