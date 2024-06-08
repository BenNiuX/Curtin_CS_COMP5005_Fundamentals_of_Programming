#
# Author: Ben Niu
# ID    : 21678145
#
# num_for.py: Read in ten numbers and give sum of numbers
#
# Revisions: 05/03/2024 - created
#
print('Enter ten numbers...')
total = 0

for i in range(5):
    print('Enter a number (', i, ')...')
    number = int(input())
    total = total + number
print('Total is ', total)
