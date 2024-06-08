#
# machine.py - a vending machine example
#

import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'
RESET = '\033[0m'

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

columnname = ["#", "Name", "Price", "Count"]
treats = [[1, "Choco Pie", 100, 5],
          [2, "Hello Panda", 50, 10],
          [3, "Fortune Cookie", 30, 10],
          [4, "Fig Rool", 30, 10],
          [5, "Maliban Orange Cream", 30, 10],
          [6, "Maliban Custard Cream", 30, 10],
          [7, "Maliban Chocolate Cream", 30, 10],
          [8, "Eccles Cake", 80, 5],
          [9, "Wagon Wheel", 150, 1]]

columnwidth = [0, 0, 0, 0]
totalwidth = 0

for colid in range(len(columnwidth)):
    namelen = len(columnname[colid])
    treatslen = 0
    for i in range(len(treats)):
        tmplen = len(str(treats[i][colid]))
        if treatslen < tmplen:
            treatslen = tmplen
    if colid == 0 or colid == 1:
        treatslen += 1
    columnwidth[colid] = namelen
    if treatslen > namelen:
        columnwidth[colid] = treatslen
    totalwidth += columnwidth[colid]
totalwidth += 13
totalline = 3 + 1 + len(treats)

print(BOLD, '\nWelcome to the snack vending machine!\n', RESET)
print('\nThe slots are loaded with delicious treats!\n')

liketreat = 'Y'
while(liketreat == 'Y'):
    print(BOLD, "\nWould you like a treat? (Y/N)... ", RESET, end='')
    inputtreat = input()
    liketreat = inputtreat.upper()
    if liketreat == 'Y':
        print('\nWhich treat would you like?')
        for i in range(totalline):
            if i == 0 or i == 2 or i == totalline - 1:
                print(BLUE, '+', end='')
                print('-'*(totalwidth-2), end='')
                print('+', RESET, end='')
                print()
            elif i == 1:
                print(BLUE, '|', columnname[0].rjust(columnwidth[0], " "), '|', columnname[1].ljust(columnwidth[1], " "), '|', columnname[2].ljust(columnwidth[2], " "), '|', columnname[3].ljust(columnwidth[3], " "), '|', RESET)
            else:
                goodindex = i - 3
                good = treats[goodindex]
                print(BLUE, '|', str(good[0]).rjust(columnwidth[0], " "), '|', good[1].ljust(columnwidth[1], " "), '|', ("$%.2f" % round(good[2]/100.0, 2)).rjust(columnwidth[2], " "), '|', str(good[3]).rjust(columnwidth[3], " "), '|', RESET)
        inputselect = int(input('    Enter your selection: '))
        if inputselect >= 1 and inputselect <= len(treats):
            good = treats[inputselect-1]
            print('    That will be : $%.2f' % round(good[2]/100.0, 2))
            if good[3] - 1 < 0:
                print(RED, "Oh deart! We are all out of", good[1], RESET)
            else:
                good[3] -= 1
                print('Enjoy your treat!')
            time.sleep(2)
            for j in range(totalline + 7):
                print(LINE_UP, end=LINE_CLEAR)
else:
    print(BOLD, '\nGlad to be of service!', RESET)
