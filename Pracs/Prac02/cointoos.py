#
# cointoss.py - simulate tossing a coin multiple times
#
import random
coin = ['heads', 'tails']
heads = 0
tails = 0
trials = 1000
inputtrials = input('Please input the number of tosses: ')
trials = int(inputtrials)
print('\nCOIN TOSS\n')
for index in range(trials):
    if random.choice(coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1
print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')
