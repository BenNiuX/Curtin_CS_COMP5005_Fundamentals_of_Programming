#
# Student Name: Ben Niu
# Student ID  : 21678145
#
# test5.py: Simulate spread of disease through a population 
#            using SIR model 
# 
# Based on SIR model:
#    Shiflet&Shiflet Module 4.3 Modeling the Spread of SARS
#    and https://www.youtube.com/watch?v=k6nLfCbAzgo
#

import matplotlib.pyplot as plt
import numpy as np
import sys

Scur = 762   # number of people susceptible
Icur = 1     # number of people infected
Rcur = 0     # number of people recovered

if len(sys.argv) == 3:
    trans_const = float(sys.argv[1])
    recov_rate = float(sys.argv[2])
else:
    trans_const = 0.00218   # infectiousness of disease r = kb/N
    recov_rate = 0.5        # recovery rate a = 1/(# days infected)
simlength = 20          # number of days in simulation

resultarray = np.zeros((simlength,3)) # 2D array of floats 
resultarray[0,:] = Scur, Icur, Rcur     # record initial values

for i in range(1, simlength):
    new_infected = trans_const * Scur * Icur   # = rSI
    new_recovered = recov_rate * Icur          # = aI

    Scur = Scur - new_infected
    Icur = Icur + new_infected - new_recovered
    Rcur = Rcur + new_recovered

    resultarray[i,:] = Scur, Icur, Rcur

plt.figure(f"SIR Model with r:{trans_const}, a:{recov_rate}")
plt.title(f"SIR Model with r:{trans_const}, a:{recov_rate}")
plt.plot(range(simlength), resultarray[:,0], "k-")
plt.plot(range(simlength), resultarray[:,1], "r^")
plt.plot(range(simlength), resultarray[:,2], "gD")
plt.xlabel("# Days")
plt.xticks(range(simlength))
plt.ylabel("# People")
plt.savefig(f"r={trans_const}_a={recov_rate}.png")
#plt.show()
print("\tScur   \t\tIcur    \tRcur")
print(resultarray)

