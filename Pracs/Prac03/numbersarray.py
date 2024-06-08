#
# Author: Ben Niu
# ID    : 21678145
#
# numbersarray.py: Read ten numbers give sum, min, max & mean
#
# Revisions: 19/03/2024 - created
#
import numpy as np
import matplotlib.pyplot as plt

numarray = np.zeros(10)       # create an empty 10 element array

print('Enter ten numbers...')

for i in range(len(numarray)):
    print('Enter a number (', i, ')...')
    numarray[i] = int(input())

print('Total is ', numarray.sum())
print('Min is ', numarray.min(), 'Max is ', numarray.max())
print('Average is ', numarray.mean())

times = range(1, len(numarray) + 1)
plt.plot(times, numarray, 'ro')
plt.title('Read Ten Numbers')
plt.ylabel('Your Input Number')
plt.show()
