#
# Name : Ben Niu
# ID   : 21678145
#
# animals.py - define Animal class and Cat/Dog/Bird classes
#
class Animal():
    myclass = None

    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed

    def printit(self):
        print('Name:', self.name)
        print('DOB:', self.dob)
        print('Colour:', self.colour)
        print('Breed:', self.breed)
        print('Class:', self.myclass)

class Cat(Animal):
    myclass = "Cat"

class Dog(Animal):
    myclass = "Dog"

class Bird(Animal):
    myclass = "Bird"