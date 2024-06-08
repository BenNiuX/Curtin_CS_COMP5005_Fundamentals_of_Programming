"""
PracTest1.py: Read name & age and print an ASCII birthday cake

Student Name: Ben Niu
Student ID  : 21678145
"""

myname = "Ben Niu"
myyear = 1990
thisyear = 2024
myage = thisyear - myyear
verifiedpass = False

print(f"Hello, my name is {myname}")
yourname = input("What is your name? ")
youryear = 0
age = 0

while not verifiedpass:
    youryear = input("What year were you born? ")
    age = thisyear - int(youryear)
    if age <= 0 or age >= 120:
        print("Input year error, please retry!!!")
    else:
        verifiedpass = True

if myage > age:
    print("I'm older")
elif myage < age:
    print("You're older")
else:
    print("We're the same age")
print()
print(f"Birthday greetings, {yourname} the aged!")
print(f"Here's a cake with {age} candles!")
print()
for row in range(8):
    if row == 0:
        for i in range(age):
            if i % 2 == 1:
                print("*", end='')
            else:
                print(" ", end='')
    elif row == 1:
        for i in range(age):
            if i % 2 == 0:
                print("*", end='')
            else:
                print("|", end='')
    elif row == 2:
        for i in range(age):
            if i % 2 == 0:
                print("|", end='')
            else:
                print(" ", end='')
    elif row == 3 or row == 5 or row == 7:
        for i in range(age):
            print("#", end='')
    elif row == 4 or row == 6:
        for i in range(age):
            print("=", end='')
    print()
