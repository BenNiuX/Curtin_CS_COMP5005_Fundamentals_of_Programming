"""
pup.py - assess and plot comparison of different types of dogs

Student Name   : Ben Niu
Student Number : 21678145

"""

import matplotlib.pyplot as plt
import numpy as np

categories = ["Name", "Size", "Friendly", "Clever", "Strong"]

plist = [["Pug", 1, 3, 3, 1],
         ["Shar Pei", 3, 3, 4, 3],
         ["German Sheperd", 4, 2, 4, 4],
         ["Chihauhau", 1, 2, 3, 1]]

plt.figure('Task 0')
plt.plot([1,5,3,6])
plt.show()

DBG = False

plt.figure('Task 1')
plt.bar(categories[1:], plist[0][1:], 0.8)
plt.title(f"Ratings for {plist[0][0]}")
plt.ylim(0, 5)
plt.show()

plt.figure('Task 2')
plt.plot(categories[1:], plist[0][1:],
         categories[1:], plist[1][1:],
         categories[1:], plist[2][1:],
         categories[1:], plist[3][1:])
plt.title('Ratings for all dogs')
plt.ylim(0, 5)
plt.show()

f = plt.figure('Task 3')
f.set_tight_layout(True)
nums = [221, 222, 223, 224]
colors = ["brown", "grey", "black", "tan"]
for i in range(len(nums)):
    plt.subplot(nums[i])
    plt.bar(categories[1:], plist[i][1:], 0.8, color=colors[i])
    plt.title(f"Ratings for {plist[i][0]}")
    plt.ylim(0, 5)
plt.show()

fig, ax = plt.subplots(num='Task 4')
width = 0.2
x = np.arange(len(plist))
if DBG: print("X:", x)
parray = np.array(plist)
if DBG: print("parray:", parray)
names = parray[:,0]
if DBG: print("names:", names)
values = parray[:, 1:]
if DBG: print("values:", values)
values = np.array(values, dtype=int)
if DBG: print("values (int):", values)
for i in range(len(plist)):
    offset = width * (len(plist) - i)
    if DBG: print(x + offset, values[i], width, names[i])
    rects = ax.bar(x + offset, values[i], width, label=names[i], color=colors[i])
ax.set_title('Ratings for all dogs')
if DBG: print(ax.get_ylim())
ax.set_ylim(0, 5)
if DBG: print(ax.get_ylim())
ax.set_xticks(x + width * 3)
ax.set_xticklabels(categories[1:])
ax.legend(loc='upper right')
width, height = fig.get_size_inches()
if DBG: print(width, height)
fig.set_size_inches(width * 1.1, height * 1.3)
if DBG: print(fig.get_size_inches())
fig.tight_layout()
if DBG: print(ax.get_ylim())
plt.show()
