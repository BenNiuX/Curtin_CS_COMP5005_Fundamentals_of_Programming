#
# dosage4hr.py - simulates the amount of aspirin in the system
#
import matplotlib.pyplot as plt
import numpy as np
import math

half_life = 3.2           # elimination of aspirin
#plasma_volume = 3000      # volume of plasma (adult)
plasma_volume = 2700
dose = 2 * 325 * 1000     # two tablets @ 325mg @ unit conversion
aspirin_in_plasma = dose  # initial dose
MEC = 150.0   # approximate concentration for effectiveness
MTC = 350.0   # approximate concentration for toxicity

elimination_constant = -math.log(0.5)/half_life
elimination = elimination_constant * aspirin_in_plasma
plasma_concentration = aspirin_in_plasma/plasma_volume

simulation_time = 96 #8
time_step_size = 0.1
num_steps = int(simulation_time/time_step_size)
cumulative_time = 0.0

values = np.zeros(num_steps)
skip_count = 0
for time_step in range (int(num_steps)):
    values[time_step] = plasma_concentration
    elimination = elimination_constant * time_step_size * aspirin_in_plasma
    aspirin_in_plasma -= elimination
    # plasma_concentration = aspirin_in_plasma/plasma_volume
    # if time_step % 40 == 0:
    if time_step % 60 == 0:
        skip_count += 1
        if skip_count % 6 != 0:
            aspirin_in_plasma = aspirin_in_plasma + dose
    plasma_concentration = aspirin_in_plasma/plasma_volume


# print(values)

times = np.linspace(0, simulation_time - time_step_size, num_steps)

MECline = np.full(num_steps, MEC)
MTCline = np.full(num_steps, MTC)

plt.figure()
#plt.title('Aspirin in Plasma')
#plt.title('Aspirin: 6 hourly, Plasma: 2700')
plt.title('Aspirin: 6 hourly, skip every 4th, Plasma: 2700')
#plt.text(0+1, 350+10, 'Mean toxic Concentration', None, color='red')
#plt.text(0+1, 150+10, 'Mean Effective Corcentration', None, color='green')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration')
# plt.plot(times, values)

plt.plot(times, values, '-', times, MECline, 'g-', times, MTCline, 'r-')

plt.show()


