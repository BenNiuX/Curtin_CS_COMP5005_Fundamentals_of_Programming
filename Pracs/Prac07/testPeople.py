from people import Address, Person, Staff, Student, Postgrad, Undergrad

print('#### People Test Program ###')
testAdd = Address('10', 'Downing St', 'Carlisle', '6101')
testPerson = Person('Winston Churchill', '30/11/1874', testAdd)
testPerson.displayPerson()
# Test 1 more Person
testPerson2 = Person('Ben Niu', '18/01/1990', testAdd)
testPerson2.displayPerson()
print()

# Test Staff
testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
testPerson2 = Staff('Professor Awesome', '1/6/61', testAdd2, '12345J')
testPerson2.displayPerson()
print()

# Test Student
testStu = Student('STU Name', '18/01/1990', testAdd2, '21678145')
testStu.displayPerson()
print()

# Test Postgrad
testPostgrad = Postgrad('Postgrad Name', '1/01/2000', testAdd2, '216781')
testPostgrad.displayPerson()
print()

# Test Undergrad
testUndergrad = Undergrad('Undergrad Name', '11/10/2002', testAdd2, '216')
testUndergrad.displayPerson()
print()
