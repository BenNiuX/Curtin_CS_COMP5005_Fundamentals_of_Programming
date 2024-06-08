#
# Name : Ben Niu
# ID   : 21678145
#
# heatsource.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

def calcheat(subarray):
    result = 0.1 * (subarray.sum() + subarray[1,1])
    return result

# create heat source
hlist = []
fileobj = open('heatsource2.csv', 'r')
for line in fileobj:
    line_s = line.strip()
    ints = [float(x) for x in line_s.split(',')]
    hlist.append(ints)
fileobj.close()
size = len(hlist)
harray = np.array(hlist)
curr = harray.copy()

print(curr)
plt.figure('Step=0')
plt.imshow(curr, cmap=plt.cm.hot)
plt.show()

next = np.zeros((size,size))

for timestep in range(100):
    for r in range(1, size-1):
        for c in range(1, size-1):
            next[r,c] = calcheat(curr[r-1:r+2,c-1:c+2])

    for r in range(size):
        for c in range(size):
            if harray[r,c] > next[r,c]:
                next[r,c] = harray[r,c]
    np.where(harray > next, harray, next)
    print("Time step: ", timestep)
    print(next)
    curr = next.copy()
    plt.figure(f'Step={timestep+1}')
    plt.imshow(curr, cmap=plt.cm.hot)
    plt.show()
