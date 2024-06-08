import random
num_trials = 3000000

ncirc = 0
r = 1.0    # radius of circle
r2 = r*r

for i in range(num_trials):
    x = random.random()
    y = random.random()
    if ((x*x + y**2) <= r2):
        ncirc += 1

pi = 4.0 * ncirc / num_trials

print("\nFor ", num_trials, " trials, pi = ", pi)
