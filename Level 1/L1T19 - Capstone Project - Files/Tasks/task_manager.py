#=====importing libraries===========
'''This is the section where you will import libraries'''
# Making use of datetime libraries to get the current date and/or check datetime enter by the user
from datetime import datetime

def func():
    """
    The following program is a task manager where users can add tasks or view all available tasks if
    they have a user account. Only the admin can make new users in this program.
    Args:
        Prompts the user for login details such as username and password.
        Depending on the users inputs various different menus will be displayed where
        either data is view or stored in a text file.
    Returns:
        Storing data in either 'user.txt' or 'task.txt' for various information.
    """

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
# Declares and sets the login_details as a dictionary.
login_details = {}

# Opens and reads the specified text file then stores the data in Key: Value
# for the above declared dictionary, if file doesn't exits program will be exited.
try :
    with open('user.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split(", ")
            login_details[key] = value
except FileNotFoundError:
    print("File does not exist closing program.")
    exit()

while True:
    # Asks the user for their username and password and checks if they exist and is correct.
    try:
        username, password = input("Please enter your Username and Password: (separated by a space) \n").split(" ")
        
        # Checks to see i username exists in the login_details dictionary.
        if username in login_details:
            # Checks to see if password exists at the value where the Key = username (Key: value in dictionary)
            if password in login_details[username]:
                break
            else:
                print("Invalid password ")
        else:
            print("Invalid username.")
    except ValueError:
        print("Invalid input")

while True:
    try:
        # Opens and reads the text file again to update the dictionary incase new data has been added.
        # If file doesn't exits program will be exited.
        with open('user.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split(", ")
                login_details[key] = value
    except FileNotFoundError:
        print("File does not exit closing program.")
        exit()

    if username != "admin":
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
    else: 
        # Present the menu for an admin 
        # make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()

    if menu == 'r':
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        
        # Checks to see if the current user is admin
        if username == "admin":
            while True:
                try:
                    new_user = input("Please enter a username: (without any spaces)\n")
                    if not new_user:
                        # Forces a ValueError if new_user is empty
                        raise ValueError("Username can't be empty, please try again.")
                    elif new_user in login_details.keys():
                        # Forces a ValueError if new_user already exists
                        raise ValueError("Username already exists, please try again.")
                    # Check to see if any spaces exits 
                    elif ' ' in new_user: 
                        raise ValueError("Username contains a space please try again.")
                    else:
                        new_pass = input("Please enter a password: (without any spaces)\n")
                        if not new_pass:
                            raise ValueError("Password can't be empty, please try again.")
                        elif new_pass in login_details.values():
                            raise ValueError("Password already exists, please try again.")
                        elif new_pass == new_user:
                            raise ValueError("Your username and password can't be the same, please try again.")
                        elif ' ' in new_pass:
                            raise ValueError("Password contains a space please try again.")
                        else:
                            confirm_pass = input("Please re-enter your password:\n")
                            if confirm_pass == new_pass:
                                try:
                                    # Writes the new_user and new_pass to the 'user.txt' file in the correct format.
                                    with open('user.txt', 'a') as file:
                                        file.write(f"\n{new_user}, {new_pass}")
                                    print("New user has been registered.")
                                    break
                                except FileNotFoundError:
                                    print("File does not exit closing program.")
                                    exit()
                            else:
                                raise ValueError("Passwords does not match, please try again.")                                

                except ValueError as error:
                    print(error)

        else:
            print("You don't have the required permissions to create users.")

    elif menu == 'a':
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''

        while True:
            try:
                user = input("Which user will the task be assigned to?  ")
                if not user:
                    # Forces a ValueError if user is empty
                    raise ValueError("Invalid input, please try again.")
                elif not user in login_details.keys():
                    # Forces a ValueError if user doest not exit exists
                    raise ValueError("User does not exist, please try again.")
                else:
                    task = input("What is the task ?  ")
                    if not task:
                        raise ValueError("Task cant be empty, please try again.")
                    else:
                        task_desc = input("Please add a detailed description of the task.\n")
                        if not task_desc:
                            raise ValueError("Task description cant be empty, please try again.")
                        else:
                            date = input("Please enter the due date for the task (DD/MM/YYYY e.g. 31/12/2024):   ")
                            if not date:
                                raise ValueError("Due date cant be empty, please try again.")
                            else:
                                try:
                                    day, month, year = date.split("/")
                                    day = int(day)
                                    month = int(month)
                                    year = int(year)

                                    # Found the information about datetime here.
                                    # https://docs.python.org/3/library/datetime.html#format-codes
                                    date_now = datetime.now() # Gets and sets the current date and time to dat_now variable
                                    due_date = datetime(year, month, day)
                                    
                                    # Checks to see if the date has passed or not
                                    if due_date.date() < date_now.date():
                                        print("The date has already passed, please try again.")

                                    # Checks to see if the due_date is in the future compared to date_now.
                                    elif due_date.date() > date_now.date():
                                        # Sets the variables in a specific format e.g. 01 Jan 2000 ("%d %b %Y")
                                        date_assigned = date_now.strftime("%d %b %Y")
                                        due_date = due_date.strftime("%d %b %Y")
                                        try:
                                            # Appends the new data to the 'tasks.txt' file in the correct format.
                                            with open('tasks.txt', 'a') as file:
                                                file.write(f"\n{user}, {task}, {task_desc}, {date_assigned}, {due_date}, No")
                                            print("New task has successfully be created.")
                                            break
                                        except FileNotFoundError:
                                            print("File does not exit closing program.")
                                            exit()
                                except ValueError:
                                    print("Invalid date please try again.")

            except ValueError as error:
                print(error)

    elif menu == 'va':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
        # Reads for 'task.txt. and displays it in an easy to ready format.
        with open('tasks.txt', 'r') as file:
            for line in file:
                user, task, task_desc, date_assigned, due_date, task_status = line.strip().split(", ")

                # Found this for a solid line here
                # https://stackoverflow.com/questions/65561243/print-a-horizontal-line-in-python
                print(u'\u2500' * 79)
                print(f"Task:                       {task}")
                print(f"Assigned to:                {user}")
                print(f"Date assigned:              {date_assigned}")
                print(f"Due date:                   {due_date}")
                print(f"Task Complete?              {task_status}")
                print(f"Task description:\n {task_desc}")
                print(u'\u2500' * 79)

    elif menu == 'vm':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        
        # Reads for 'task.txt' and displays it in an easy to ready format.
        no_task = 1
        with open('tasks.txt', 'r') as file:
            for line in file:
                user, task, task_desc, date_assigned, due_date, task_status = line.strip().split(", ")

                if user == username:
                # Found this for a solid line here
                # https://stackoverflow.com/questions/65561243/print-a-horizontal-line-in-python
                    print(u'\u2500' * 79)
                    print(f"Task:                       {task}")
                    print(f"Assigned to:                {user}")
                    print(f"Date assigned:              {date_assigned}")
                    print(f"Due date:                   {due_date}")
                    print(f"Task Complete?              {task_status}")
                    print(f"Task description:\n {task_desc}")
                    print(u'\u2500' * 79)
                else:
                    # The no_task variable ensures that the results is only displayed once each time this menu is called.
                    if no_task == 1:
                        print(u'\u2500' * 79)
                        print(f"The current user: {username} has no tasks assigned to them")
                        print(u'\u2500' * 79)
                        no_task += 1

    elif menu == 'ds':
        # Declares and sets the variables to 0 to ensure accurate calculations.
        total_tasks = 0
        total_users = 0

        with open('tasks.txt', 'r') as file:
            for line in file:
                total_tasks += 1

        with open('user.txt', 'r') as file:
            for line in file:
                total_users += 1

        # The above reads and calculates the total number of task and users.
        # Then prints the total_users and total_tasks in a easy to read format.
        # Found this for a solid line here
        # https://stackoverflow.com/questions/65561243/print-a-horizontal-line-in-python
        print(u'\u2500' * 79)
        print(f"The total number of tasks:          {total_tasks}")
        print(f"The total number of users:          {total_users}")
        print(u'\u2500' * 79)

    elif menu == 'e':
        print('Goodbye!!!')
        # Stops the program.
        exit()

    else:
        print("You have entered an invalid input. Please try again")