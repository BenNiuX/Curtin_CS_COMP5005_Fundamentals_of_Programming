#
# Name : Ben Niu
# ID   : 21678145
#
# banking.py - simulating bank account transactions
#
from accounts import BankAccount

bankaccount = BankAccount('Everyday', '007', 3000)

print('Bank Account Operation\n')
bucket = []
choice = input('Enter selection: (W)ithdrawal, (D)eposit, (I)nterest, (B)lance, e(X)it...')
while choice[0].upper() != 'X':
    if choice[0].upper() == 'W':
        print('Enter amount...')
        amount = input()
        try:
            amount = int(amount)
            bankaccount.withdraw(amount)
            print("Withdraw success")
        except:
            print("Input amount error!")
    elif choice[0].upper() == 'D':
        print('Enter amount...')
        amount = input()
        try:
            amount = int(amount)
            bankaccount.deposit(amount)
            print("Deposit success")
        except:
            print("Input amount error!")
    elif choice[0].upper() == 'I':
        bankaccount.add_interest()
        print("Add interest success")
    elif choice[0].upper() == 'B':
        print(f"Balance: {bankaccount.balance}")
    else:
        print('Invalid selection.')
    choice = input('Enter selection: (W)ithdrawal, (D)eposit, (I)nterest, (B)lance, e(X)it...')
print('\nGOODBY!\n')