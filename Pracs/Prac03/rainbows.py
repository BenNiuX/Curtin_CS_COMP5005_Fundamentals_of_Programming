#
# Author: Ben Niu
# ID    : 21678145
#
# rainbows.py: Draw a rainbow using pyplot
#
# Revisions: 19/03/2024 - created
#
import matplotlib.pyplot as plt
import math
import numpy as np

res = 4
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
for r in range(10, 3, -1):
    colour = colours.pop(0)
    size = r * res * 2 + 1
    xarray = np.zeros(size)
    arcarray = np.zeros(size)
    for i in range(-res * r, res * r+1):
        xarray[i+res*r] = i
        arcarray[i+res*r] = math.sqrt((res*r)**2 - i**2)
    plt.plot(xarray, arcarray, color=colour, marker="o")
plt.title("Rainbow")
plt.show()

