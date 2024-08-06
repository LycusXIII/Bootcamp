"""
The following program is a task manager where users can add tasks or
view all available tasks if they have a user account. Only the admin
can make new users in this program.
"""
import sys
import os
from datetime import datetime


def reg_user():
    '''
    Registers a new user if the current user is the admin.

    This function prompts the admin for a new username and password,
    checks the input for emptiness, spaces and if the password is the
    same as the username then stores the new user info to the 
    'user.txt' file.
    Args:
        None
    Returns:
        None
    '''
    if username != "admin":
        print("You don't have permissions to create users.")
        return
    while True:
        try:
            new_user = input("Please enter a username: (no spaces)\n").lower()

            # Checks the username for emptiness
            if not new_user:
                raise ValueError("Username can't be empty")
            # Checks for existing usernames
            if new_user in login_details:
                raise ValueError("Username already exists")
            # Checks for spaces
            if ' ' in new_user:
                raise ValueError("Username cannot contains spaces.")

            new_pass = input("Please enter a password: (no spaces)\n")
            # Checks the password for emptiness
            if not new_pass:
                raise ValueError("Password can't be empty.")
            # Checks is password is the same as username
            if new_pass == new_user:
                raise ValueError("Username and password cannot be the same")
            # Checks for spaces
            if ' ' in new_pass:
                raise ValueError("Password contains a space.")
            confirm_pass = input("Please re-enter your password:\n")
            # Checks if passwords match
            if confirm_pass != new_pass:
                raise ValueError("Passwords does not match.")
            # Checks if file exits before storing the info to 'user.txt'
            try:
                if not os.path.exists('user.txt'):
                    raise FileNotFoundError
                with open('user.txt', 'a', encoding='utf-8') as reg_file:
                    reg_file.write(f"\n{new_user}, {new_pass}")
                    print("New user has been registered.")
                    break
            except FileNotFoundError:
                print("File does not exit closing program.")
                sys.exit(0)
        except ValueError as error:
            print(error)


def add_task():
    '''
    Allows the user to add more tasks inside the 'tasks.txt'
    Args:
        None
    Returns:
        None
    '''
    while True:
        try:
            user = input("Which user will the task be assigned to?  ")
            # Checks if user is empty
            if not user:
                raise ValueError("Invalid input, please try again.")
            # Checks if user exists in login_details dictionary
            if not user in login_details:
                raise ValueError("User does not exist, please try again.")
            # Checks if task is empty
            task = input("What is the task ?  ")
            if not task:
                raise ValueError("Task cant be empty, please try again.")
            task_desc = input("Please add a detailed description.\n")
            # Checks if task_desc is empty
            if not task_desc:
                raise ValueError("Task description cant be empty")
            date_assigned, due_date = validate_date()
            try:
                # Checks to see if 'user.txt' exists
                if not os.path.exists('user.txt'):
                    raise FileNotFoundError
                # Appends the new data to the 'tasks.txt'
                with open('tasks.txt', 'a', encoding='utf-8') as add_task_file:
                    add_task_file.write(f"\n{user}, {task}, {task_desc}, "+
                                f"{date_assigned}, {due_date}, No")
                print("New task has successfully be created.")
                break
            except FileNotFoundError:
                print("File does not exit closing program.")
                sys.exit(0)
            except ValueError:
                print("Invalid date please try again.")
        except ValueError as error:
            print(error)
    # Calls function to remove any empty lines in 'tasks.txt'
    remove_empty_lines()


def view_all():
    '''
    Allows the user to view all tasks in 'tasks.txt'
    Args:
        None
    Returns:
        None
    '''
    try:
        # Checks if 'tasks.txt' exists
        if not os.path.exists('tasks.txt'):
            raise FileNotFoundError
        remove_empty_lines()
        # Reads for 'tasks.txt. and displays it in an easy to ready format.
        with open('tasks.txt', 'r', encoding='utf-8') as view_file:
            for user, task, task_desc, date_assigned, due_date, task_status in (
                view_line.strip().split(", ") for view_line in view_file):
                print('\u2500' * 79)
                print(f"Task:                       {task}")
                print(f"Assigned to:                {user}")
                print(f"Date assigned:              {date_assigned}")
                print(f"Due date:                   {due_date}")
                print(f"Task Complete?              {task_status}")
                print(f"Task description:\n {task_desc}")
                print('\u2500' * 79)
    except FileNotFoundError:
        print("File does not exit closing program.")
        sys.exit(0)


def view_mine():
    '''
    Allows the user to view all tasks for the current user.
    Args:
        None
    Returns:
        None
    '''
    remove_empty_lines()
    tasks_found = False
    task_number = 1
    # Reads form 'tasks.txt' and displays it in an easy to ready format.
    try:
        # Checks if 'tasks.txt' exists
        if not os.path.exists('tasks.txt'):
            raise FileNotFoundError
        # Reads for 'tasks.txt. and displays it in an easy to ready format.
        task_lines = {}
        with open('tasks.txt', 'r', encoding='utf-8') as mine_file:
            for line_number, mine_line in enumerate(mine_file, start=1):
                user, task, task_desc, date_assigned, due_date, task_status = (
                    mine_line.strip().split(", "))
                if user == username:
                    tasks_found = True
                    task_lines[task_number] = line_number
                    # Found this for a solid line here
                    # https://shortlurl.com/6651d993eb07a
                    print('\u2500' * 79)
                    print(f"Task:                       {task}")
                    print(f"Task number:                {task_number}")
                    print(f"Assigned to:                {user}")
                    print(f"Date assigned:              {date_assigned}")
                    print(f"Due date:                   {due_date}")
                    print(f"Task Complete?              {task_status}")
                    print(f"Task description:\n {task_desc}")
                    print('\u2500' * 79)
                    task_number += 1
        if tasks_found is False:
            print('\u2500' * 79)
            print(f"The current user: {username} has no tasks.")
            print('\u2500' * 79)
        else:
            try:
                select_task = int(input("Select a task by entering the task "
                                        + "number or by typing -1 to return "
                                        + "to main menu:\n"))
                edit_task(select_task, task_lines)
            except ValueError:
                print("Invalid input, Returning to main menu.")
    except FileNotFoundError:
        print("File does not exit closing program.")
        sys.exit(0)


def edit_task(select_task, task_lines):
    '''
    Allows the user to edit the task selected.
    Args:
        select_task (int): User input from the view_mine() function 
        representing the chosen task.
        task_lines (dict): Dictionary mapping task numbers to line 
        index in the tasks.txt file.
    Returns:
        None
    '''
    if select_task == -1:
        return
    try:
        # Checks if 'tasks.txt' exists
        if not os.path.exists('tasks.txt'):
            raise FileNotFoundError
    except FileNotFoundError:
        print("File does not exit closing program.")
        sys.exit(0)
    # Opens 'task.txt' for reading.
    with open('tasks.txt', 'r', encoding='utf-8') as edit_file:
        edit_lines = edit_file.readlines()
    if select_task not in task_lines:
        print("Invalid task selected returning to main menu")
        return
    line_index = task_lines[select_task] - 1
    edit_line = edit_lines[line_index].strip().split(", ")
    task_status = edit_line[5]
    if task_status == "Yes":
        print("Task is complete, completed tasks cant be edited."
                + " Returning to main menu.")
    if task_status == "No":
        while True:
            try:
                # Prompts the user for input then calls the functions based on
                # the users choices.
                user_choice = int(input("Would you like to:\n"
                                        + "1. Mark as complete\n"
                                        + "2. Edit the task\n"
                                        + "Type -1 to return to main menu:\n"))
                if user_choice == -1:
                    break
                elif user_choice == 1:
                    mark_task_complete(edit_lines, line_index)
                    break
                elif user_choice == 2:
                    change_task(login_details, edit_lines, line_index)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input try again.")


def mark_task_complete(mark_lines, line_index):
    '''
    Marks the selected task as complete and writes it to the 
    'tasks.txt' file.
    Args:
        mark_lines (list): all the lines of the 'tasks.txt' file
        line_index (int): The line of the selected task.
    Returns:
        None
    '''
    # Gets the right information based on the args
    # Then writes the file with the new data of the modified task data
    mark_line = mark_lines[line_index].strip().split(", ")
    user, task, task_desc, date_assigned, due_date, task_status = mark_line
    task_status = "Yes"
    mark_lines[line_index] = (f"{user}, {task}, {task_desc}, {date_assigned}, "
                              + f"{due_date}, {task_status}\n")
    with open('tasks.txt', 'w', encoding='utf-8') as mark_file:
        mark_file.writelines(mark_lines)
        print("Task has been marked as complete, returning to main menu.")
    # Calls this function to remove empty lines
    # to prevent errors from occurring
    remove_empty_lines()


def change_task(login_data, change_lines, line_index):
    '''
    Prompts the user of input and changes the selected task based 
    on user input
    Args:
        login_data (dict): Gets the dictionary containing all login 
        information.
        change_lines (list): all the lines of the 'tasks.txt' file
        line_index (int): The line of the selected task.
    Returns:
        None
    '''
    # Gets the right information based on the args
    # Then writes the file with the new data of the modified task data
    change_line = change_lines[line_index].strip().split(", ")
    user, task, task_desc, date_assigned, due_date, task_status = change_line
    while True:
        try:
            # Prompts the user for input then calls the functions
            # based on the users choices.
            user_input = int(input("What would you like to edit:\n"
                                    + "1. Assign task to a different user ?\n"
                                    + "2. Change due date ?\n"
                                    + "Type -1 to return to main menu:\n"))
            if user_input == -1:
                break
            if user_input == 1:
                new_user = input("Enter the new username of the one being "
                                +"assigned to the task:\n")
                if new_user == user:
                    print("Cant assign the same user to this task.")
                    break
                if new_user in login_data:
                    change_lines[line_index] = (f"{new_user}, {task}, "
                                    + f"{task_desc}, {date_assigned}, "
                                    + f"{due_date}, {task_status}\n")
                    with open('tasks.txt', 'w',
                              encoding='utf-8') as change_file:
                        change_file.writelines(change_lines)
                    print(f"Task has been assigned to {new_user}")
                    break
            elif user_input == 2:
                dates = validate_date()
                new_due_date = dates[1]
                change_lines[line_index] = (f"{user}, {task}, "
                                    + f"{task_desc}, {date_assigned}, "
                                    + f"{new_due_date}, {task_status}\n")
                with open('tasks.txt', 'w', encoding='utf-8') as change_file:
                    change_file.writelines(change_lines)
                print("New due date has been assigned to selected task.")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, please try again.")
            continue
    remove_empty_lines()


def display_statistic():
    '''
    This function checks if 'task_overview.txt' and 'user_overview.txt' exists
    if not function generate_task_overview() will be called to generate the 2
    text files. After which will then read and display the contents for the 2 
    text files.
    Args:
        None
    Returns:
        None
    '''
    # Checks if 'task_overview.txt' and 'user_overview.txt' exists
    if not os.path.exists('task_overview.txt') and not os.path.exists(
        'user_overview.txt'):
        generate_task_overview()
    # Opens 'task_overview.txt' for reading to display its contents
    print("Task overview:")
    with open('task_overview.txt', 'r', encoding='utf-8') as tasks_data:
        display_tasks = tasks_data.read()
        print(display_tasks)
    # Opens 'user_overview.txt' for reading to display its contents
    print("User overview:")
    print("------------------------------------------------------------")
    with open('user_overview.txt', 'r', encoding='utf-8') as users_data:
        display_users = users_data.read()
        print(display_users)


def generate_task_overview():
    '''
    This function creates a text files called 'task_overview.txt'
    and writes the data specified to that file.
    Args:
        None
    Returns:
        None
    '''
    # Checks if 'tasks.txt' exists
    if not os.path.exists('tasks.txt'):
        raise FileNotFoundError
    # Sets and declares variables to act like counters
    total_tasks = 0
    total_completed_tasks = 0
    total_uncompleted_tasks = 0
    overdue_tasks = 0
    # Reads for 'tasks.txt. and displays it in an easy to ready format.
    with open('tasks.txt', 'r', encoding='utf-8') as generate_file:
        for generate_line in generate_file:
            # Strips and splits the data in line to index
            index = generate_line.strip().split(", ")
            # Assigning the only 2 indexes used to variables
            due_date = index[4]
            task_status = index[5]
            total_tasks += 1
            if task_status == "Yes":
                total_completed_tasks += 1
            elif task_status == "No":
                total_uncompleted_tasks += 1
                date = datetime.strptime(due_date, "%d %b %Y")
                current_date = datetime.now()
                if date < current_date:
                    overdue_tasks += 1
        # Calculates the percentages for the required fields.
        if total_uncompleted_tasks == 0 and total_tasks >= 0:
            percentage_incomplete = 0
        else:
            percentage_incomplete = (total_uncompleted_tasks/total_tasks) * 100
        if overdue_tasks == 0 and total_tasks >= 0:
            percentage_overdue = 0
        else:
            percentage_overdue = (overdue_tasks/total_tasks) * 100

    # Opens to write to file in a readable format
    with open('task_overview.txt', 'w+', encoding='utf-8') as file:
        file.writelines([
      "\u2500" * 45 + "\n",
      f"Total number of tasks:              {total_tasks}\n",
      f"Total number of completed tasks:    {total_tasks - overdue_tasks}\n",
      f"Total number of uncompleted tasks:  {overdue_tasks}\n",
      f"Total number of overdue tasks:      {overdue_tasks}\n",
      f"Percentage of incomplete tasks:     {percentage_incomplete:.0f}%\n",
      f"Percentage of overdue tasks:        {percentage_overdue:.0f}%\n",
      "\u2500" * 45 + "\n"
    ])
    generate_user_overview(total_tasks)


def generate_user_overview(tasks):
    '''
    This function creates an empty text file called 'user_overview.txt'
    and writes the data specified to that file. (has to create and/or 
    empty the file to ensure accurate date is written to the file)
    Args:
        tasks: gets the total number of tasks from 
        generate_task_overview() function.
    Returns:
        None
    '''
    # Value of tasks gets passed from generate_task_overview() function.
    total_tasks = tasks
    total_users = 0
    # Creates and/or clears the file.
    with open('user_overview.txt', 'w+', encoding='utf-8') as file:
        pass
    # Reads for 'tasks.txt. and displays it in an easy to ready format.
    with open('user.txt', 'r', encoding='utf-8') as user_txt:
        for line_1 in user_txt:
            # Only assigns the first word to the variable
            user_1 = line_1.strip().split(", ")[0]
            total_users += 1
            while True:
                # Sets and declares variables to act like counters
                total_tasks_for_user = 0
                complete_tasks = 0
                incomplete_tasks = 0
                overdue_tasks = 0
                with open('tasks.txt', 'r', encoding='utf-8') as task_txt:
                    for line_2 in task_txt:
                        # Strips and splits the data in line_2 to index
                        index = line_2.strip().split(", ")
                        # Assigning the only 2 indexes used to variables
                        user_2 = index[0]
                        due_date_2 = index[4]
                        task_status_2 = index[5]
                        if user_2 == user_1:
                            total_tasks_for_user += 1
                            if task_status_2 == "Yes":
                                complete_tasks += 1
                            elif task_status_2 == "No":
                                incomplete_tasks += 1
                                date = datetime.strptime(
                                    due_date_2, "%d %b %Y")
                                current_date = datetime.now()
                                if date < current_date:
                                    overdue_tasks += 1
                data = calculate_percentages(total_tasks,
                            total_tasks_for_user, complete_tasks,
                            incomplete_tasks, overdue_tasks)
                total_assigned_percent = data[0]
                complete_percentage = data[1]
                incomplete_percentage = data[2]
                percentage_overdue = data[3]
                # Opens to write to file in a readable format
                with open('user_overview.txt', 'a+', encoding='utf-8'
                            ) as file:
                    file.writelines([
                    f"Details for {user_1}:\n",
                    "Total number of tasks assigned:   "
                    + f"{total_tasks_for_user}\n",
                    "The percentage of tasks assigned: "
                    + f"{total_assigned_percent:.0f}%\n",
                    "Percentage of tasks completed:    "
                    + f"{complete_percentage:.0f}%\n",
                    "Percentage of tasks incomplete:   "
                    + f"{incomplete_percentage:.0f}%\n",
                    "The percentage of overdue tasks:  "
                    + f"{percentage_overdue:.0f}%\n",
                    "Percentage of tasks overdue:      "
                    + f"{percentage_overdue:.0f}%\n",
                    "\u2500" * 45 + "\n"
                    ])
                break
    with open('user_overview.txt', 'a+', encoding='utf-8') as file:
        file.writelines([
            f"Total number of users:               {total_users}\n",
            f"Total number of tasks:               {total_tasks}\n",
            '\u2500' * 45 + "\n"
            ])


def calculate_percentages(total_tasks, total_tasks_for_user,
                complete_tasks, incomplete_tasks, overdue_tasks):
    '''
    Calculates the percentage for various tasks.
    Args:
        total_tasks: Total number of tasks
        total_tasks_for_user: Total tasks assigned to current user.
        complete_tasks: Total completed tasks for current user.
        incomplete_tasks: Total incomplete tasks for current user.
        overdue_tasks: Total of overdue tasks for current user.
    Returns:

    '''
    total_assigned_percent = 0
    complete_percentage = 0
    # Calculates the percentages for the required fields then returns.
    if total_tasks_for_user == 0 and total_tasks >= 0:
        total_assigned_percent = 0
    else:
        total_assigned_percent = (total_tasks_for_user/total_tasks) * 100
    if complete_tasks == 0 and total_tasks_for_user > 0:
        complete_percentage = 0
    elif complete_tasks == 0 and total_tasks_for_user == 0:
        complete_percentage = 100
    else:
        complete_percentage = (complete_tasks/total_tasks_for_user) * 100
    if incomplete_tasks == 0 and total_tasks_for_user >= 0:
        incomplete_percentage = 0
    else:
        incomplete_percentage = (incomplete_tasks/total_tasks_for_user) * 100
    if overdue_tasks == 0 and total_tasks >= 0:
        percentage_overdue = 0
    else:
        percentage_overdue = (overdue_tasks/total_tasks_for_user) * 100
    return (total_assigned_percent, complete_percentage, incomplete_percentage,
    percentage_overdue)


def validate_date():
    '''
    This function prompts a user to enter a date then checks the date
    for emptiness and if its the right format.
    Args:
        None.
    Returns:
        tuple: A tuple containing 2 strings (date_assigned and due_date)
    '''
    # Found the information about datetime here.
    # https://docs.python.org/3/library/datetime.html#format-codes
    # Gets and sets the current date and time to dat_now variable
    while True:
        try:
            print("Please enter the due date for the task in DD/MM/YYYY "
                  +"(e.g. 31/12/2024):")
            date = input("")
            if not date:
                raise ValueError("Date cant be empty, please try again.")
            day, month, year = date.split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            date_now = datetime.now()
            # Converts the due_date to datetime format
            due_date = datetime(year, month, day)
            if due_date.date() < date_now.date():
                print("The date has already passed.")
                continue
            if due_date.date() == date_now.date():
                print("Date cant be changed to the same day.")
                continue
            if due_date.date() > date_now.date():
                # Changes to format of the variables below
                date_assigned = date_now.strftime("%d %b %Y")
                due_date = due_date.strftime("%d %b %Y")
                return date_assigned, due_date
        except ValueError:
            print("Invalid date format.")


def remove_empty_lines():
    '''
    This function removes the empty lines (lines containing only whitespaces)
    in 'tasks.txt' to ensure errors wont occur.
    Args:
        None
    Returns:
        None
    '''
    # Resources used to make this function
    # https://www.geeksforgeeks.org/how-to-remove-blank-lines-from-a-txt-file-in-python/
    # https://www.geeksforgeeks.org/python-seek-function/
    # https://www.w3schools.com/python/ref_file_truncate.asp
    with open('tasks.txt', 'r+', encoding='utf-8') as remove_lines_file:
        lines = remove_lines_file.readlines()
        # Removes leading/trailing whitespaces
        filtered_lines = [line for line in lines if line.strip()]

        # Checks to see if there are any lines and if the last line is empty
        # (after removing whitespaces)
        if filtered_lines and not filtered_lines[-1].strip():
            filtered_lines.pop()
        # Moves the file pointer to the start of the file (index 0)
        remove_lines_file.seek(0)
        # Clears to file to write the filtered lines
        remove_lines_file.truncate()
        # Writes the filtered_lines to the file
        remove_lines_file.writelines(filtered_lines)


# Declares and sets the login_details as a dictionary.
login_details = {}

# Opens and reads the specified text file then stores the data in Key:
# Value for the above declared dictionary, if file doesn't exits program
# will be exited.
try :
    with open('user.txt', 'r', encoding='utf-8') as login_file:
        for line in login_file:
            key, value = line.strip().split(", ")
            login_details[key] = value
except FileNotFoundError:
    print("File does not exist closing program.")
    sys.exit(0)

while True:
    # Asks the user for their username and password and checks if they exist and is correct.
    try:
        username = input("Please enter your Username: ").lower()
        password = input("Please enter your Password: ")
        # Checks to see i username exists in the login_details dictionary.
        if username in login_details:
            # Checks to see if password exists at the value where the Key = username
            # (Key: value in dictionary)
            if login_details[username] == password:
                break
            print("Invalid password ")
        else:
            print("Invalid username.")
    except ValueError:
        print("Invalid input")

while True:
    try:
        # Opens and reads the text file again to update the dictionary incase new data
        # has been added. If file doesn't exits program will be exited.
        with open('user.txt', 'r', encoding='utf-8') as load_data_file:
            for line in load_data_file:
                key, value = line.strip().split(", ")
                login_details[key] = value
    except FileNotFoundError:
        print("File does not exit closing program.")
        sys.exit(0)
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
gr - generate reports
ds - display statistics
e - exit
: ''').lower()

    if menu == 'r':
        # This sections calls red_user() wit the login_details dictionary
        # to add new users to the 'user.txt' file if the current logged
        # in user is admin.
        reg_user()
    elif menu == 'a':
        # This section calls add_task() function to add a new task to tasks.txt file
        add_task()
    elif menu == 'va':
        # This sections calls view_all() function to view all the contents of
        # 'tasks.txt' in a readable format.
        view_all()
    elif menu == 'vm':
        # This sections calls view_mine() function to view all the current
        # users tasks from 'tasks.txt'
        view_mine()
    elif menu == 'gr':
        # This section calls generate_task_overview() function to
        # generate 2 text files namely 'task_overview.txt'
        # and 'user_overview.txt'
        generate_task_overview()
        print("The 'task_overview.txt' has been generated.")
        print("The 'user_overview.txt' has been generated.")
    elif menu == 'ds':
        # This section calls display_statistic() function to calculate
        # the total number of users and tasks and displays the results
        # in a readable format.
        display_statistic()
    elif menu == 'e':
        print('Goodbye!!!')
        # Stops the program.
        sys.exit(0)
    else:
        print("You have entered an invalid input. Please try again")
