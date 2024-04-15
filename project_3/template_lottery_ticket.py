import random

class LotteryTicket:

    def __init__(self, info):
        # Split the info string into multiple pieces separated by ‘,’ or ‘/’
        tokens = info.split(",")
        self.first = tokens[0].strip()
        self.last = tokens[1].strip()
        # strip the full birthday and then extract the day, month, year
        birthday = tokens[5].strip()
        pieces = birthday.split("/")
        self.day = int(pieces[1])
        self.month = int(pieces[0])
        self.year = int(pieces[2])
        # resume with the six ticket numbers
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
        return self.zipcode

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def get_prize(self):
        return self.prize

    def get_mega_ball(self):
        return self.mega_ball

    def get_nums(self):
        return self.nums

    def has_ball(self, val):
        return val in self.nums

    def has_mega_ball(self, val):
        return val == self.mega_ball

    def __str__(self):
        return f"{self.first} {self.last}\n{self.city}, {self.state} {self.zipcode}\n{self.nums}\nPrize: ${self.prize:.2f}"


class LotteryMachine:

    def __init__(self):
        self.tickets = []
        self.nums = []
        self.mega_ball = 0

    def get_ticket_count(self):
        return len(self.tickets)

    def get_mega_ball(self):
        return self.mega_ball

    def get_nums(self):
        return self.nums

    def add_ticket(self, t):
        self.tickets.append(t)

    def read_tickets(self, filename):
        with open(filename) as file:
            for entry in file:
                t = LotteryTicket(entry)
                self.add_ticket(t)

    def draw_random_numbers(self):
        self.nums = random.sample(range(1, 76), 5)
        self.mega_ball = random.randint(1, 15)

    def count_matches(self, t):
        count = 0
        for num in t.get_nums():
            if num in self.nums:
                count += 1
        return count

    def make_payouts(self):
        for ticket in self.tickets:
            matches = self.count_matches(ticket)
            if matches == 5 and ticket.has_mega_ball(self.mega_ball):
                ticket.prize = 5000000.00
            elif matches == 5:
                ticket.prize = 1000000.00
            elif matches == 4 and ticket.has_mega_ball(self.mega_ball):
                ticket.prize = 5000.00
            elif matches == 4:
                ticket.prize = 500.00
            elif matches == 3 and ticket.has_mega_ball(self.mega_ball):
                ticket.prize = 50.00
            elif matches == 3:
                ticket.prize = 5.00
            elif matches == 2 and ticket.has_mega_ball(self.mega_ball):
                ticket.prize = 5.00
            elif matches == 1 and ticket.has_mega_ball(self.mega_ball):
                ticket.prize = 2.00
            elif matches == 0 and ticket.has_mega_ball(self.mega_ball):
                ticket.prize = 1.00

    def __str__(self):
        return f"Selected Numbers: {' '.join(map(str, self.nums))} {self.mega_ball}"

    def draw_ticket(self):
        self.draw_random_numbers()
        self.make_payouts()

    def test_ticket(self, b1, b2, b3, b4, b5, mega):
        self.nums = [b1, b2, b3, b4, b5]
        self.mega_ball = mega
        self.make_payouts()

    def print_report(self, st):
        tickets_in_state = [t for t in self.tickets if t.get_state() == st]
        if not tickets_in_state:
            return 0
        print(self)
        print(f"Tickets sold in {st}: {len(tickets_in_state)}")
        average_prize = sum(t.get_prize() for t in tickets_in_state) / len(tickets_in_state)
        print(f"Average prize amount: ${average_prize:.2f}")
        biggest_winner = max(tickets_in_state, key=lambda t: t.get_prize())
        print(f"Biggest Winner\n{biggest_winner}")
        return len(tickets_in_state)

    def get_oldest_player(self):
        oldest_ticket = min(self.tickets, key=lambda t: (t.get_year(), t.get_month(), t.get_day()))
        return oldest_ticket

    def get_big_winner(self):
        biggest_winner = max(self.tickets, key=lambda t: t.get_prize())
        return biggest_winner

    def get_big_winners(self, amount):
        big_winners = [t for t in self.tickets if t.get_prize() >= amount]
        return big_winners

    def print_big_winners(self, amount):
        big_winners = self.get_big_winners(amount)
        if not big_winners:
            print("No big winners")
        else:
            print("Big Winners ($50 or higher)")
            for winner in big_winners:
                print(winner)

    def multiple_drawings(self, num):
        jackpot = 5000000.00
        winner = False
        draw_count = 0
        while not winner and draw_count < num:
            self.draw_ticket()
            draw_count += 1
            biggest_winner = self.get_big_winner()
            if biggest_winner.get_prize() == jackpot:
                winner = True
            else:
                jackpot += 1500000.00
        print(f"Number of drawings: {draw_count}")
        print(f"Biggest Winner\n{biggest_winner}")
        return jackpot


if __name__ == '__main__':
    lm = LotteryMachine()
    lm.read_tickets("ticket_info.txt")
    print(lm.multiple_drawings(100))