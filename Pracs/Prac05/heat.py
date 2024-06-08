#
# Name : Ben Niu
# ID   : 21678145
#
# heat.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

size = 10
total_step = 50
init_value = 10
curr = np.zeros((size,size))
print(curr)
plt.figure('0')
plt.imshow(curr, cmap=plt.cm.hot)
plt.show()
for i in range(size):
    curr[i,0] = init_value #10

plt.figure('Step=0')
plt.imshow(curr, cmap=plt.cm.hot)
plt.show()

next = np.zeros((size,size))

for timestep in range(total_step):
    for r in range(1, size-1):
        for c in range(1, size-1):
            next[r,c] = (curr[r-1,c-1]*0.1 + curr[r-1,c]*0.1
                + curr[r-1,c+1]*0.1 + curr[r,c-1]*0.1
                + curr[r,c]*0.2 + curr[r,c+1]*0.1
                + curr[r+1,c-1]*0.1 + curr[r+1,c]*0.1
                + curr[r+1,c+1]*0.1)
            next[r,c] = 0.1 * (curr[r-1:r+2,c-1:c+2].sum() + curr[r,c])

    for i in range(size):
        next[i,0] = init_value #10

    print("Time step: ", timestep)
    print(next)
    curr = next.copy()
    plt.figure(f'Step={timestep+1}')
    plt.imshow(curr, cmap=plt.cm.hot)
    plt.show()
