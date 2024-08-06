"""
The program demonstrates class inheritances by having a class
that represents a general course offered by hyperiondev.
"""


class Course:
    '''
    This class sets the main details of the course.
    '''
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        '''
        Prints out instructions on how to contact the institute about
        the course.
        '''
        print("Please contact us by visiting", self.contact_website)

    def head_office_location():
        '''
        Prints out the head officer location.
        '''
        print("The head office is located at Cape Town.")


class OOPCourse(Course):
    '''
    This class contains more details about the specific course
    OOP Fundamentals. (OOP = Object-Oriented Programming)
    This class inherits from the Class Course.
    '''

    def __init__(self, description="OOP Fundamentals",
                 trainer="Mr Anon A. Mouse"):
        '''
        Initializes an OOPCourse object with a description and trainer
        name and have default values assigned to each.
        Args:
            description : A description of the course. Default value is set to
            "OOP Fundamentals".
            trainer: The name of the trainer assigned to this course. Default
            value is set to "Mr Anon A. Mouse".
        '''
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        '''
        Prints the information about the course description and the trainer.
        '''
        print(f"This course is about {self.description} lead by trainer"
              f" {self.trainer}")

    def show_course_id(self):
        '''
        Prints out the ID number of the course.
        '''
        print("Course ID number: #12345")


# Creates an object of the subclass and calls the methods
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
