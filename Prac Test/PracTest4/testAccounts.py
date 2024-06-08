'''
  Practical Test 4

  testAccounts.py - program to test functions of accounts.py
  
  Student Name   : Ben Niu
  Student Number : 21678145
  Date/prac time : 30/04 6pm
'''
from accounts import BankAccount, Portfolio, InsufficientFundsError

print('\n#### Bank Accounts Portfolio ####\n')
myAccounts = Portfolio()

# add code for tasks here

#e.g.
#myAccounts.addAccount("Everyday", "1111-007", 1000)
#myAccounts.deposit("Everyday",200)
NAME_CAS = "Castle"
NAME_SHR = "Shrubbery"
NAME_GRA = "Grail"
myAccounts.addAccount(NAME_CAS, "999999-1", 1000)
myAccounts.addAccount(NAME_SHR, "999999-2", 100)
myAccounts.addAccount(NAME_GRA, "999999-3", 100)

myAccounts.balances()

myAccounts.deposit(NAME_CAS, 100)
try:
  myAccounts.withdraw(NAME_SHR, 10)
except InsufficientFundsError as e:
  print("     ****  Exception: ", e)
  myAccounts.balances()

try:
  myAccounts.withdraw(NAME_SHR, 1000)
except InsufficientFundsError as e:
  print("     ****  Exception: ", e)
  myAccounts.balances()

myAccounts.deposit(NAME_GRA, 100)

print(f"\nNumber of Accounts: {myAccounts.getNumAccounts()}\n")
print(f"\nTotal Balance of Accounts: {myAccounts.getTotalBalance()}\n")

try:
  myAccounts.withdraw(NAME_GRA, 1000)
except InsufficientFundsError as e:
  print("     ****  Exception: ", e)
  myAccounts.balances()