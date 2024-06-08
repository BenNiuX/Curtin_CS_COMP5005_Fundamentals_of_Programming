#
# Author: Ben Niu
# ID    : 21678145
#
# bruces.py - let's call everyone "Bruce", to avoid confusion
#
# Revisions: 05/03/2024 - created
#
name = input("What is your name? ")
if name != "Bruce":
    print("Sorry,", name, "- your name's not Bruce?")
    print("That's going to cause a little confusion.")
    print("Mind if we call you 'Bruce' to keep it clear?")
    name = "Bruce"
else:
    print("Excellent! That saves a lot of confusion!")
print("G'day", name)
