#
# weather.py: Print min and max temps from a file
# (source: http://www.bom.gov.au/climate/)

import matplotlib.pyplot as plt

fileobj = open('marchweather.csv', 'r')

# add file reading code here
line1 = fileobj.readline()
line2 = fileobj.readline()

fileobj.close()

mins = [float(v) for v in line1.split(',')]
maxs = [float(v) for v in line2.split(',')]

dates = range(1,32)

plt.plot(dates, mins, dates, maxs)
plt.show()
