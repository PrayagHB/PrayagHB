"""
Author: Prayag Bhatt, bhatt59@purdue.edu
Assignment: 11.4 - Bank Accounts
Date: 04/03/2024

Description:
    This program gives the information about your bank account regarding the deposits and withdrawals made to the account.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
class Account:
    def __init__(self,balance):
        self.balance=balance
        print(f'New account balance: ${self.balance:.2f}')
    def deposit(self,amount):
        self.balance+=amount
        return print(f'Deposit: ${amount:.2f}')
    def withdraw(self,amount):
        if amount>self.balance:
            return print(f'Withdraw: ${amount:.2f}\nInsufficient funds. Withdrawal canceled.')
        else:
            self.balance-=amount
            return print(f'Withdraw: ${amount:.2f}')
    def get_balance(self):
        return print(f'Balance: ${self.balance:.2f}')

class Savings(Account):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate=interest_rate
    def accrue_interest(self):
        k=self.balance*(self.interest_rate/100)
        self.balance+=k
        return print(f'Interest payment: ${k:.2f}')

def main():
    #This program gives the information about your bank account regarding the deposits and withdrawals made to the account.
    x=Savings(200,10)
    x.get_balance()
    x.deposit(12.34)
    x.get_balance()
    x.withdraw(40)
    x.get_balance()
    x.withdraw(200)
    x.get_balance()
    x.accrue_interest()
    x.accrue_interest()
    x.accrue_interest()
    x.withdraw(200)
    x.get_balance()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
