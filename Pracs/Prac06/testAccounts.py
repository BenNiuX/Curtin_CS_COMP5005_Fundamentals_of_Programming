#
# Name : Ben Niu
# ID   : 21678145
#
# testAccounts.py - simulating bank account transactions using function
#

from accounts import BankAccount

def balances(a):
    total = 0
    for i in range(len(a)):
        print(f"Name: {a[i].name}\tNumber: {a[i].number}\tBalance: {a[i].balance}")
        total = total + a[i].balance
    print(f"\tTotal: {total}")

accounts = []
bank = BankAccount('Everyday', '007', 2000)
accounts.append(bank)
bank = BankAccount('Cheque A/C', '008', 3000)
accounts.append(bank)
bank = BankAccount('Term Deposit', '009', 20000)
accounts.append(bank)
balances(accounts)

print("\nDoing some transactions...\n")
accounts[0].deposit(100)
accounts[1].withdraw(500)
accounts[2].add_interest()
balances(accounts)