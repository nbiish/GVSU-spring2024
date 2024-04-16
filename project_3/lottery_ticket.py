

class LotteryTicket:

    def __init__(self, info):
        # BUILDING OUT OBJECT FROM INPUT DATA TXT FILE
        # EXAMPLE DATA: 
        # Amy, Zu, AnyCity, NC, 27834, 4/20/1960, 5, 12, 37, 39, 68, 11
        
        # Split the info string into multiple pieces separated by ‘,’ or ‘/’
        tokens = info.split(",")
        self.first = tokens[0].strip()
        self.last = tokens[1].strip()

        # strip the full address and then extract the city, state, and zip
        self.city = tokens[2].strip()
        self.state = tokens[3].strip()
        self.zip = tokens[4].strip()

        # strip the full birthday and then extract the day, month, year
        birthday = tokens[5].strip()
        pieces = birthday.split("/")
        self.day = int(pieces[1])
        self.month = int(pieces[0])
        self.year = int(pieces[2])

        self.birth_date = f"{self.year}-{self.month}-{self.day}"

        def get_birth_date(self):
            return self.birth_date
        
        def get_oldest_player(self):
            return min(self.tickets, key=lambda ticket: ticket.get_birth_date())


        # six ticket numbers
        self.num1 = int(tokens[6].strip())
        self.num2 = int(tokens[7].strip())
        self.num3 = int(tokens[8].strip())
        self.num4 = int(tokens[9].strip())
        self.num5 = int(tokens[10].strip())
        self.mega_ball = int(tokens[11].strip())

        self.nums = [int(num) for num in tokens[6:11]]
        self.prize = 0.0



    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zipcode(self):
        return self.zip

    def get_birth_date(self):
        return self.birth_date

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

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
        return f"{self.get_first()} {self.get_last()}\n{self.get_city()}, {self.get_state()} {self.get_zipcode()}\n{self.get_nums()}   {self.get_mega_ball()}\nPrize: $1.00"


if __name__ == '__main__':
    t = LotteryTicket("Louis,Laker,Allendale,MI,49401,4/20/1985,5,10,15,20,25,7")
    print(t)
    print(t.has_ball(10))
    print(t.has_mega_ball(7))
    print(t.get_nums())
    print(t.get_mega_ball())
    t.set_prize(1000000)
    print(t.prize)