def func():
    """
    Registers certain number of students based on user input for exam venu and stores the
    students IDs in a file with space for the students to sign.
    Args:
        User inputs.
    Returns:
        A filed called 'reg_form.txt' with the student IDs.
    """
# Checks to see if the user inputs a valid integer and if not asks the user for an input again.
while True:
    try:
        num_students = int(input("How many students will be registering for the exam ? (e.g. 10)\n"))
        break
    except ValueError:
        print("Invalid input.")

# Opens/Creates a file called 'reg_form.txt' if the file exists the date will be overwritten.
with open('reg_form.txt', 'w') as file:
    for i in range(num_students):
        # Checks to see if not an empty string.
        while True:
            student_id = input("Please enter your student ID: ")
            if student_id:
                # Writes the data to the file
                file.write(f"{student_id}\n")
                file.write(".................\n")
                break
            else:
                print("Invalid input. Please enter a student ID.\n")