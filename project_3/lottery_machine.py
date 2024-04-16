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
        # Returns the total number of tickets
        return len(self.tickets)

    def get_mega_ball(self):
        # Returns the mega ball number
        return self.mega_ball

    def get_nums(self):
        # Returns the list of five numbers
        return self.five_numbers

    # Initial Methods
    def add_ticket(self, t):
        # Adds a new ticket to the list of tickets
        self.tickets.append(t)

    def read_tickets(self, filename):
        # Reads tickets from a file and adds them to the list of tickets
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.add_ticket(LotteryTicket(line.strip()))

    # Helper Methods
    def draw_random_numbers(self):
        # Draw five unique random numbers from 1 to 75 and a mega ball number from 1 to 16
        self.five_numbers = random.sample(range(1, 76), 5)
        self.mega_ball = random.randint(1, 16)

    def count_matches(self, t):
        # Count the number of matching numbers between the drawn numbers and the ticket numbers
        return len(set(self.five_numbers) & set(t.get_nums()))

    def make_payouts(self):
        # Determine the prize for each ticket based on the number of matching numbers and mega ball
        for ticket in self.tickets:
            matches = self.count_matches(ticket)
            mega_ball_match = (self.mega_ball == ticket.get_mega_ball())
            if matches == 5 and mega_ball_match:
                ticket.set_prize(5000000)  # All five numbers and mega ball match
            elif matches == 5:
                ticket.set_prize(1000000)  # Only five numbers match
            elif matches == 4 and mega_ball_match:
                ticket.set_prize(5000)  # Four numbers and mega ball match
            elif matches == 4:
                ticket.set_prize(500)  # Only four numbers match
            elif matches == 3 and mega_ball_match:
                ticket.set_prize(50)  # Three numbers and mega ball match
            elif matches == 3:
                ticket.set_prize(5)  # Only three numbers match
            elif matches == 2 and mega_ball_match:
                ticket.set_prize(5)  # Two numbers and mega ball match
            elif matches == 1 and mega_ball_match:
                ticket.set_prize(2)  # One number and mega ball match
            elif mega_ball_match:
                ticket.set_prize(1)  # Only mega ball matches

    def __str__(self):
        # Returns a string representation of the selected numbers and the mega ball
        return f"Selected Numbers: {' '.join(map(str, self.five_numbers))} {self.mega_ball}"

    # Mutator Methods
    def draw_ticket(self):
        # Draws random numbers and makes payouts
        self.draw_random_numbers()
        self.make_payouts()

    def test_ticket(self, b1, b2, b3, b4, b5, mega):
        # Tests a ticket with specific numbers and makes payouts
        self.five_numbers = [b1, b2, b3, b4, b5]
        self.mega_ball = mega
        self.make_payouts()

    def print_report(self, st):
        # Filter tickets based on the state
        tickets_in_state = [ticket for ticket in self.tickets if ticket.get_state() == st]
        if not tickets_in_state:
            return 0
        # Calculate total and average prize for the state
        total_prize = sum(ticket.get_prize() for ticket in tickets_in_state)
        average_prize = total_prize / len(tickets_in_state)
        # Find the ticket with the highest prize in the state
        biggest_winner = max(tickets_in_state, key=lambda ticket: ticket.get_prize())
        # Print the report
        print(f"State: {st}")
        print(f"Selected Numbers: {' '.join(map(str, self.five_numbers))} {self.mega_ball}")
        print(f"Number of Tickets: {len(tickets_in_state)}")
        print(f"Average Prize: {average_prize}")
        print(f"Biggest Winner: {biggest_winner}")
        return len(tickets_in_state)

    def get_oldest_player(self):
        # Find the ticket with the earliest birth date
        return min(self.tickets, key=lambda ticket: ticket.get_birth_date())

    def get_big_winner(self):
        # Find the ticket with the highest prize
        return max(self.tickets, key=lambda ticket: ticket.get_prize())

    def get_big_winners(self, amount):
        # Filter tickets based on the prize amount
        return [ticket for ticket in self.tickets if ticket.get_prize() > amount]

    def print_big_winners(self, amount):
        # Print the tickets with prizes greater than or equal to the specified amount
        big_winners = self.get_big_winners(amount)
        for ticket in big_winners:
            print(ticket)

    def multiple_drawings(self, num):
        # Initialize variables for the biggest winner
        big_winner_name = None
        top_prize = 0

        # Perform multiple drawings
        for _ in range(num):
            if self.mega_winner:
                break

            # Draw numbers and make payouts
            self.draw_random_numbers()
            self.make_payouts()

            # Update the biggest winner if necessary
            winner = self.get_big_winner()
            if winner.get_prize() > top_prize:
                top_prize = winner.get_prize()
                big_winner_name = winner.__str__()

            # Check if the jackpot was won
            if self.count_matches(winner) == 6:
                self.mega_winner = True
            else:
                # Increase the jackpot if it wasn't won
                self.jackpot += 1500000

        # Print the results of the multiple drawings
        print(f"Number of Drawings: {num}")
        print(f"Biggest Winner: {big_winner_name}")

        return top_prize


def main():
    machine = LotteryMachine()
    machine.read_tickets("ticket_info.txt")
    machine.draw_random_numbers()
    print("Result from Report for Texas")
    machine.print_report("TX")  # replace "NY" with the state you want to print the report for
    print("Result for Biggest Winner")
    big_winner = machine.get_big_winner()
    print(big_winner)
    print("Result for Multiple Drawings")
    print(machine.multiple_drawings(100))
    print("Result for Big Winners ($50 or higher)")
    big_winners = machine.get_big_winners(50)
    for winner in big_winners:
        print(winner)
    print(len(big_winners), "winning tickets")


if __name__ == "__main__":
    main()

    lm = LotteryMachine()
    lm.read_tickets("ticket_info.txt")
    print(lm.multiple_drawings(100))
