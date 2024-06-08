class Address():
    def __init__(self, number, street, suburb, postcode): 
        self.number = number
        self.street = street
        self.suburb = suburb
        self.postcode = postcode

    def __str__(self):
        return(self.number + ' ' + self.street + ', ' + self.suburb + ', ' + self.postcode)

class DodInvalid(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"DodInvalid: {self.message}"

class Person():
    def __init__(self, name, dob, address): 
        self.name = name
        self.validateDob(dob)
        self.dob = dob
        self.address = address

    def displayPerson(self):
        print('Name: ', self.name, '\tDOB: ', self.dob) 
        print(' Address: ', str(self.address))

    def validateDob(self, dob):
        if dob and len(dob.strip()) > 0:
            dmy = dob.strip().split('/')
            try:
                if len(dmy) == 3:
                    day = int(dmy[0])
                    month = int(dmy[1])
                    year = int(dmy[2])
                    if day <= 0 or day >31:
                        raise DodInvalid(f"Input day error: {dob}")
                    if month <= 0 or month > 12:
                        raise DodInvalid(f"Input month error: {dob}")
            except Exception as e:
                raise DodInvalid(str(e))


class Staff(Person):
    myclass = 'Staff'
    def __init__(self, name, dob, address, id): 
        super().__init__(name, dob, address) 
        self.id = id

    def displayPerson(self): 
        super().displayPerson() 
        print(' StaffID: ', self.id)

class Student(Person):
    myclass = 'Student'
    def __init__(self, name, dob, address, id): 
        super().__init__(name, dob, address) 
        self.id = id

    def displayPerson(self): 
        super().displayPerson() 
        print(' StudentID: ', self.id)

class Postgrad(Student):
    myclass = 'Postgrad'
    # def __init__(self, name, dob, address, id):
    #     super().__init__(name, dob, address, id)

class Undergrad(Student):
    myclass = 'Undergrad'
    # def __init__(self, name, dob, address, id):
    #     super().__init__(name, dob, address, id)