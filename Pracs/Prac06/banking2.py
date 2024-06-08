#
# Name : Ben Niu
# ID   : 21678145
#
# banking2.py - simulating bank account transactions using function
#
from accounts import BankAccount

def chooseTrans():
    available_input = ['W', 'D', 'I', 'B', 'X']
    while True:
        choice = input('Enter selection: (W)ithdrawal, (D)eposit, (I)nterest, (B)lance, e(X)it...')
        choice = choice[0].upper()
        if choice in available_input:
            return choice
        else:
            print("Input error, try again!")

bankaccount = BankAccount('Everyday', '007', 3000)

print('Bank Account Operation\n')
bucket = []
choice = chooseTrans()
while choice != 'X':
    if choice == 'W':
        print('Enter amount...')
        amount = input()
        try:
            amount = int(amount)
            bankaccount.withdraw(amount)
            print("Withdraw success")
        except:
            print("Input amount error!")
    elif choice == 'D':
        print('Enter amount...')
        amount = input()
        try:
            amount = int(amount)
            bankaccount.deposit(amount)
            print("Deposit success")
        except:
            print("Input amount error!")
    elif choice == 'I':
        bankaccount.add_interest()
        print("Add interest success")
    elif choice == 'B':
        print(f"Balance: {bankaccount.balance}")
    else:
        print('Invalid selection.')
    choice = chooseTrans()
print('\nGOODBY!\n')