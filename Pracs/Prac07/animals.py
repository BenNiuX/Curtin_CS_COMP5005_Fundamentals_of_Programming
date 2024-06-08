#
# Name : Ben Niu
# ID   : 21678145
#
# animals.py - define Animal class and Cat/Dog/Bird/Shelter classes
#
class Animal():
    myclass = "Animal"

    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed

    def __str__(self):
        return(self.name + '|' + self.dob + '|' + self.colour + '|' + self.breed)

    def printit(self):
        spacing = 5 - len(self.myclass) 
        print(self.myclass.upper(), spacing*' ' + ': ', self.name,'\tDOB: ', 
                self.dob,'\tColour: ', self.colour,'\tBreed: ', self.breed)

class Dog(Animal):
    myclass = "Dog"

class Cat(Animal):
    myclass = "Cat"

class Bird(Animal):
    myclass = "Bird"

class Shelter():

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.processing = [] 
        self.available = [] 
        self.adopted = []
        
    def displayProcessing(self):
        print('Current processing list:') 
        for a in self.processing:
            a.printit() 
        print()
    
    def displayAvailable(self):
        print('Current available list:') 
        for a in self.available:
            a.printit() 
        print()
    
    def displayAdopted(self):
        print('Current adopted list:') 
        for a in self.adopted:
            a.printit() 
        print()
    
    def displayAll(self):
        self.displayProcessing()
        self.displayAvailable()
        self.displayAdopted()
    
    def newAnimal(self, type, name, dob, colour, breed):
        temp = None
        if type == 'Dog':
            temp = Dog(name, dob, colour, breed) 
        elif type == 'Cat':
            temp = Cat(name, dob, colour, breed) 
        elif type == 'Bird':
            temp = Bird(name, dob, colour, breed) 
        else:
            print('Error, unknown animal type: ', type) 
        if temp:
            self.processing.append(temp) 
            print('Added ', name, ' to processing list') 
        
    def makeAvailable(self, name):
        tmp = None
        for ani in self.processing:
            if name == ani.name:
                tmp = ani
                self.available.append(ani)
        if tmp: self.processing.remove(tmp)

    def makeAdopted(self, name):
        tmp = None
        for ani in self.available:
            if name == ani.name:
                tmp = ani
                self.adopted.append(ani)
        if tmp: self.available.remove(tmp)