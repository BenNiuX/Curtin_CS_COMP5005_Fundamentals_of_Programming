pops = {'New South Wales': 7757843,
 'Victoria' : 6100877,
 'Queensland' : 4860448,
 'South Australia' : 1710804,
 'Western Australia' : 2623164,
 'Tasmania': 519783,
 'Northern Territory' : 245657,
 'Australian Capital Territory': 398349}
print(pops['Victoria'])
for location in pops:
    print(location)
for k in pops.keys():
    print(k, ' : ', pops[k])