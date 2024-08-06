'''
This program asks for user input and based on the age of the user
either a Adult class object of a Child object will be created
and print out the users name and if they to young or old enough to
drive.
'''


class Adult():
    '''
    This class represents attributes of an adult.
    '''

    def __init__(self, name, age, eye_colour, hair_colour):
        '''
        Initializes an objects with these attributes.
        '''
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        '''
        Prints out a message with the users name that they are old
        enough to drive.
        '''
        print(f"{self.name} is old enough to drive.")


class Child(Adult):
    '''
    The class represents attributes of an child.
    This class inherits from class Adult.
    '''

    def can_drive(self):
        '''
        Prints out a message with the users name that they are to
        young to drive.
        '''
        print(f"{self.name} is too young to drive.")


validation_checking = False
while not validation_checking:
    try:
        # Gets user input and test for valid inputs.
        name = input("Enter your name:  ")
        if not name.isalpha():
            raise ValueError("Name must only have letters.")

        age = int(input("Please enter your age:  "))
        if age < 0:
            raise ValueError("Age cannot be negative.")

        eye_colour = input("Enter your eye colour:  ")
        if not eye_colour.isalpha():
            raise ValueError("Eye colour must only have letters.")

        hair_colour = input("Enter your hair_colour:  ")
        if not hair_colour.isalpha():
            raise ValueError("Hair colour must only have letters")

        validation_checking = True
    except ValueError as error:
        print(error)
        print("Invalid input please try again.")

# Test to see if the user is 18 or older
if age >= 18:
    adult_1 = Adult(name, age, eye_colour, hair_colour)
    adult_1.can_drive()
else:
    child_1 = Child(name, age, eye_colour, hair_colour)
    child_1.can_drive()
