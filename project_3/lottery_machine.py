import random
from lottery_ticket import LotteryTicket

class LotteryMachine:
    def __init__(self):
        self.tickets = []  # list of LotteryTicket
        self.five_numbers = []  # list of five numbers
        self.mega_ball = None  # mega ball number
        self.jackpot = 5000000  # jackpot amount
        self.mega_winner = False


    # Accessor Methods
    def get_ticket_count(self):
        return len(self.tickets)

    def get_mega_ball(self):
        return self.mega_ball

    def get_nums(self):
        return self.five_numbers

    # Initial Methods
    def add_ticket(self, t):
        self.tickets.append(t)

    def read_tickets(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.add_ticket(LotteryTicket(line.strip()))

    # Helper Methods
    def draw_random_numbers(self):
        self.five_numbers = random.sample(range(1, 76), 5)
        self.mega_ball = random.randint(1, 16)

    def count_matches(self, t):
        return len(set(self.five_numbers) & set(t.get_nums()))

    def make_payouts(self):
        for ticket in self.tickets:
            matches = self.count_matches(ticket)
            mega_ball_match = (self.mega_ball == ticket.get_mega_ball())
            if matches == 5 and mega_ball_match:
                ticket.set_prize(5000000)
            elif matches == 5:
                ticket.set_prize(1000000)
            elif matches == 4 and mega_ball_match:
                ticket.set_prize(5000)
            elif matches == 4:
                ticket.set_prize(500)
            elif matches == 3 and mega_ball_match:
                ticket.set_prize(50)
            elif matches == 3:
                ticket.set_prize(5)
            elif matches == 2 and mega_ball_match:
                ticket.set_prize(5)
            elif matches == 1 and mega_ball_match:
                ticket.set_prize(2)
            elif mega_ball_match:
                ticket.set_prize(1)

    def __str__(self):
        return f"Selected Numbers: {' '.join(map(str, self.five_numbers))} {self.mega_ball}"

    # Mutator Methods
    def draw_ticket(self):
        self.draw_random_numbers()
        self.make_payouts()

    def test_ticket(self, b1, b2, b3, b4, b5, mega):
        self.five_numbers = [b1, b2, b3, b4, b5]
        self.mega_ball = mega
        self.make_payouts()

    def print_report(self, st):
        tickets_in_state = [ticket for ticket in self.tickets if ticket.get_state() == st]
        if not tickets_in_state:
            return 0
        total_prize = sum(ticket.get_prize() for ticket in tickets_in_state)
        average_prize = total_prize / len(tickets_in_state)
        biggest_winner = max(tickets_in_state, key=lambda ticket: ticket.get_prize())
        print(f"State: {st}")
        print(f"Selected Numbers: {' '.join(map(str, self.five_numbers))} {self.mega_ball}")
        print(f"Number of Tickets: {len(tickets_in_state)}")
        print(f"Average Prize: {average_prize}")
        print(f"Biggest Winner: {biggest_winner}")
        return len(tickets_in_state)

    def get_oldest_player(self):
        return min(self.tickets, key=lambda ticket: ticket.get_birth_date())

    def get_big_winner(self):
        return max(self.tickets, key=lambda ticket: ticket.get_prize())

    def get_big_winners(self, amount):
        return [ticket for ticket in self.tickets if ticket.get_prize() >= amount]

    def print_big_winners(self, amount):
        big_winners = self.get_big_winners(amount)
        for ticket in big_winners:
            print(ticket)


# BONUS SECTION
    def multiple_drawings(self, num):
        big_winner_name = None
        top_prize = 0

        for _ in range(num):
            if self.mega_winner:
                break

            self.draw_random_numbers()
            self.make_payouts()

            winner = self.get_big_winner()
            if winner.get_prize() > top_prize:
                top_prize = winner.get_prize()
                big_winner_name = winner.__str__()

            if self.count_matches(winner) == 6:
                self.mega_winner = True
            else:
                self.jackpot += 1500000

        print(f"Number of Drawings: {num}")
        print(f"Biggest Winner: {big_winner_name}")

        return top_prize

def main():
    machine = LotteryMachine()
    machine.read_tickets("ticket_info.txt")
    machine.draw_random_numbers()
    print(machine)
    print("Ticket Count:", machine.get_ticket_count())
    machine.print_report("MI")  # replace "NY" with the state you want to print the report for

if __name__ == "__main__":
    
    lm = LotteryMachine()
    lm.read_tickets("ticket_info.txt")
    print(lm.multiple_drawings(100))