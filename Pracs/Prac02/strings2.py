#
# strings2.py: Read in a string and print it in forward
#           using a loop and a method call

instring = input('Enter a string... ')

# *** add (2) upper and (3) duplicating code here
instring = instring.upper()
instring = instring*2
print('New string is:', instring)
# Forward with a while loop
print('Forward string is : ', end='')
index = 1
while index < len(instring)-1:
    print(instring[index], end='')
    index = index + 2
print()

# Forward with a for-range loop
print('Forward string is : ', end='')
for index in range(1, len(instring)-1, 2):
    print(instring[index], end='')
print()

# Forward with slicing
print('Forward string is :', instring[1:-1:2])
print('Forward string is :', instring[1:len(instring)-1:2])
