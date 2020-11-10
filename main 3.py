from random import randint

class BankAccount:
  def __init__(self, full_name):
    self.full_name = full_name
    self.account_number = randint(10000000, 99999999)
    self.routing_number = 123456789
    self.balance = 0.00

  def deposit(self, amount):
    self.balance += amount
    print(f'Amount Deposited: ${amount}')

  def withdraw(self, amount):
    self.balance -= amount
    if(self.balance >= 0.00):
      print(f'Amount Withdrawn: ${amount}')
    elif(self.balance < 0.00):
      print(f'Insufficient funds. You will now receive an overdraft fee of $10')
      self.balance -= 10.00

  def get_balance(self):
    print(f'Your current balance is ${self.balance}')
    return self.balance

  def add_interest(self):
    interest = self.balance * 0.00083
    self.balance += interest
    print(f'Balance this month after interest: {self.balance}')

  def print_receipt(self):
    print(f'{self.full_name} \n Account No.: {self.account_number} \n Routing No.: {self.routing_number} \n Balance: ${self.balance}')

Bobs_account = BankAccount('Bob Stone')
BankAccount.deposit(Bobs_account, 400.0)
BankAccount.get_balance(Bobs_account)
BankAccount.withdraw(Bobs_account, 75.0)
BankAccount.get_balance(Bobs_account)
BankAccount.add_interest(Bobs_account)
BankAccount.print_receipt(Bobs_account)

print("\n")

Timmys_account = BankAccount('Little Timmy')
BankAccount.deposit(Timmys_account, 10.0)
BankAccount.get_balance(Timmys_account)
BankAccount.withdraw(Timmys_account, 6.0)
BankAccount.get_balance(Timmys_account)
BankAccount.print_receipt(Timmys_account)

print("\n")

Emilias_account = BankAccount('Emilia Everheart III')
BankAccount.deposit(Emilias_account, 200000.0)
BankAccount.get_balance(Emilias_account)
BankAccount.withdraw(Emilias_account, 250000.0)
BankAccount.get_balance(Emilias_account)
BankAccount.print_receipt(Emilias_account)