#
# Name : Ben Niu
# ID   : 21678145
#
# testAnimals.py - testing animals including Cat/Dog/Bird
#

from animals import Cat, Dog, Bird

garfield = Cat('Garfield', '1/1/1978', 'Orange', 'Tabby')

garfield.printit()

print(garfield)

dog1 = Dog('dog1', '1/2/1989', 'Black', 'breed_dog1')
dog1.printit()
print(dog1)

bird1 = Bird('bird1', '2/1/2000', 'White', 'breed_bird1')
bird1.printit()
print(bird1)

animallist = []
fileobj = open('animals.csv', 'r')
lines = fileobj.readlines()
fileobj.close()
for line in lines:
    splitline = line.split(',')
    animtype = splitline[0]
    animal = None
    if Cat.myclass == animtype:
        animal = Cat(splitline[1].strip(), splitline[2].strip(), splitline[3].strip(), splitline[4].strip())
    elif Dog.myclass == animtype:
        animal = Dog(splitline[1], splitline[2].strip(), splitline[3].strip(), splitline[4].strip())
    elif Bird.myclass == animtype:
        animal = Bird(splitline[1], splitline[2].strip(), splitline[3].strip(), splitline[4].strip())
    if animal:
        animal.printit()
        animallist.append(animal)
print(animallist)