#
# marchweather2.py: Print min, max temps and 9am, 3pm temps
#
import matplotlib.pyplot as plt

fileobj = open('marchweatherfull.csv', 'r')
data = fileobj.readlines()
fileobj.close()

mins = []
maxs = []
nines = []
threes = []

for line in data:
    splitline = line.split(',')
    mins.append(float(splitline[2]))
    maxs.append(float(splitline[3]))
    nines.append(float(splitline[10]))
    threes.append(float(splitline[16]))

dates = range(1,32)

plt.plot(dates, mins, dates, maxs, dates, nines, dates, threes)
plt.show()

file2 = open('marchout.csv', 'w')
for i in range(len(mins)):
    file2.write(f"{mins[i]},{maxs[i]},{nines[i]},{threes[i]}\n")
file2.close()
