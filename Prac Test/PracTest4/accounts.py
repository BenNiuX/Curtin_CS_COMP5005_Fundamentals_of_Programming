'''
  Practical Test 4

  accounts.py - class for bank account portfolio
  
  Student Name   : Ben Niu
  Student Number : 21678145
  Date/prac time : 30/04 6pm
'''

class Portfolio ():

    def __init__(self):
        self.accounts = []

    def addAccount(self, name, number, balance):
        self.accounts.append(BankAccount(name, number, balance))

    def deposit(self, name, amount):
        '''
        deposit - deposits amount into account with matching name
        
        name - name of account (string)
        amount - amount to be deposited (float/int)
        '''
        temp = None
        for acct in self.accounts:
            if acct.name == name:
                temp = acct
        if temp:
            print("---> Depositing $" + str(amount) + " into account " + name)
            temp.deposit(amount)
            print("         Complete")

    def withdraw(self, name, amount):
        '''
        withdraw - withdraws amount into account with matching name
        
        name - name of account (string)
        amount - amount to be withdrawn (float/int)
        '''
        temp = None
        for acct in self.accounts:
            if acct.name == name:
                temp = acct
        if temp:
            print("---> Withdrawing $" + str(amount) + " from account " + name)
            if temp.bal < amount:
                raise InsufficientFundsError('Withdrawal exceeds balance')
            else:
                temp.withdraw(amount)
                print("         Complete")
        else:
            raise AccountNotFoundError('Acount not found')


    def balances(self):
        print('\n<----------------  Balances of All Accounts  ---------------->')
        total = 0
        for i in range(len(self.accounts)):
            t_str = "\t\t"
            if len(self.accounts[i].name) > 8:
                t_str = "\t"
            print("Name:", self.accounts[i].name, t_str + "Number: ", self.accounts[i].num, \
                "\tBalance: ", self.accounts[i].bal)
            total = total + self.accounts[i].bal
        print("\t\t\t\t\t\tTotal:   ", total)
        print('<------------------------------------------------------------>\n')
        print()

    def getNumAccounts(self):
        '''
        getNumAccounts - returns the number of accounts in the portfolio
        
        enter your code below
        '''
        return len(self.accounts)

    def getTotalBalance(self):
        '''
        getNumAccounts - returns the number of accounts in the poartfolio
        
        enter your code below - the balances code may help
        '''
        total = 0
        for account in self.accounts:
            total += account.bal
        return total

    
class BankAccount ():

    def __init__(self, name, number, balance):
        self.name = name
        self.num = number
        self.bal = balance

    def withdraw(self, amount):
            self.bal = self.bal - amount

    def deposit(self, amount):
        self.bal = self.bal + amount

class InsufficientFundsError(Exception):
    '''
    Insufficient Funds error - to be raised where a transaction exceeds available balance
    '''
    pass

class AccountNotFoundError(Exception):
    '''
    Account Not Found error - to be raised where account name doesn't match accounts in portfolio
    '''
    pass
