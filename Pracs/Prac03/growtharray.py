#
# Author: Ben Niu
# ID    : 21678145
#
# growtharray.py - simulatin of unconstrained growth
#                 using array to store data to plot
#
# Revisions: 19/03/2024 - created
#
import matplotlib.pyplot as plt
import numpy as np

print("\nSIMULATION - Unconstrained Growth\n")
length = 100
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step
timearray = np.zeros(int(num_iter)+1)
poparray = np.zeros(int(num_iter)+1)
print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (sim length * time step per hour): ", num_iter)
print("Growth step (growth rate per time step): ", growth_step)

print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)
times=[0]                    # list of times, initial value is zero
pops=[100]                   # list of populations, initial is 100
timearray[0]=0
poparray[0]=100

for i in range(1, int(num_iter) + 1 ):
    growth = growth_step * population
    population = population + growth
    time = i * time_step
    times.append(time)       # add current time
    pops.append(population)  # add current pop
    timearray[i]=time
    poparray[i]=population
    print("Time: ", time, " \tGrowth: ", growth, "\tPopulation: ", population)
print("\nPROCESSING COMPLETE.\n")

plt.title('Prac 3.3: Unconstrained Growth')
plt.plot(timearray, poparray, 'r')        # plot times and pops
plt.xlabel('Hour')
plt.ylabel('Population')
plt.show()
