'''
The following program aims to simulate emails using OOP.
'''
# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object
import sys


class Email():
    '''
    This class simulates an email using OOP.
    An Email object has the following attributes:
        email_address - email address of the sender.
        subject_line - subject line of the email.
        email_content - the content of the email.
        has_been-read - a boolean indication if the email was read or
        not.
    This class has a method to manage the email object:
        mark_as_read() - Marks the email as read by changing the value
        of has_been_read to true (default = false)
    '''
    # Declare the class variable, with default value, for emails.
    # Class variables
    # Used as default value for emails read status.
    has_been_read = False

    # Initialise the instance variables for emails.
    # Constructor method with instance variables
    def __init__(self, email_address, subject_line, email_content):
        '''
        Initializes and 'Email' object.
        Args:
            email_address - email address of the sender.
            subject_line - subject line of the email.
            email_content - the content of the email.
        '''
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False
    # to True.
    def mark_as_read(self):
        '''
        Marks the email as read by changing has_been_read to True.
        Args:
            None
        Returns:
            None
        '''
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []


# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():
    '''
    This function creates 3 sample emails and adds them to the inbox
    list.
    '''
    # Creates 3 sample emails and add it to the Inbox list.
    email1 = Email(
        "johndoe@gmail.com",
        "Hello World 1",
        '''This is sample email 1.
Making use of multiple lines to simulate an emails content.
Have a nice day.\n''')

    email2 = Email(
        "janedoe@gmail.com",
        "Hello World 2",
        '''This is sample email 2.
Making use of multiple lines to simulate an emails content.
Have a nice day.\n''')

    email3 = Email(
        "randomperson@gmail.com",
        "Hello World 3",
        '''This is sample email 3.
Making use of multiple lines to simulate an emails content.
Have a nice day.\n''')

    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)


def list_emails():
    '''
    This function lists all the emails stored in inbox[] and prints out
    the subject_line for each one of them with a corresponding number.
    Args:
        None
    Returns:
        None
    '''
    # Create a function which prints the email’s subject_line,
    # along with a corresponding number.
    for index, subjects in enumerate(inbox):
        print(f"{index}  {subjects.subject_line}")


def read_email(index):
    '''
    This function displays the selected email for the user in readable
    format also updates the has_been_read variable to true.
    Args:
        index: the index of the selected email.
    Returns:
        None
    '''
    # Create a function which displays a selected email.
    # Once displayed, call the class method to set its
    # 'has_been_read' variable to True.
    if index < 0 or index >= len(inbox):
        print("Invalid input. Please try again.")
        return

    email = inbox[index]
    print(f"\nFrom:       {email.email_address}")
    print(f"Subject:    {email.subject_line}")
    print(f"{email.email_content}")
    email.mark_as_read()
    print(f"Email from {email.email_address} marked as read.")
    inbox[index] = email


# --- Email Program --- #
# Call the function to populate the inbox with sample data.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        # add logic here to read an email
        list_emails()
        selected_email = int(input(
            "Please enter the number of the email you want to read:  "))
        read_email(selected_email)
    elif user_choice == 2:
        # add logic here to view unread emails
        for subjects in inbox:
            if not subjects.has_been_read:
                print(f"{subjects.subject_line}")
    elif user_choice == 3:
        # add logic here to quit application
        sys.exit(0)
    else:
        print("Oops - incorrect input.")
