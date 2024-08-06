# Needed to enable this for the file reading to work
# https://stackoverflow.com/questions/69769139/relative-file-path-is-not-recognized-by-python-in-vscode

def modify_file():
    """
    Reads data from file called 'DOB.txt' and formats the data to Name and Birthdates sections.
    Args:
        File provided.
    Returns:
        Outputs the contents of the file to the terminal formated to the desired results.
    """

print(modify_file.__doc__)  #Testing docstring

# Declares and sets variables to empty lists
names = []
birthdates = []

try:
    # Opens and reads the text file called DOB.txt
    with open ('DOB.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Takes the data from line and strips and splits it inot a list.
        # Each index of the list containing a single word or numbers without spaces.
        temp_line = line.strip()
        temp_line = line.split()

        # Declares and sets variables to empty list to be used as temporary storage
        temp_names = []
        temp_birthdates = []
        no_numbers = True

        for data in temp_line:
            # Checks if the value inside data is only alphabet (a-z)
            # Making use of a boolean variable called no_numbers
            # to ensure the temp_line is split between names and birthdates 
            if data.isalpha() and no_numbers == True:
                temp_names.append(data)
            else:
                no_numbers = False
                temp_birthdates.append(data)

        # Using the temp variables below to append the fullname and birthdate to
        # a single string each, then stored.
        temp_names = " ".join(temp_names)
        temp_birthdates = " ".join(temp_birthdates)
        names.append(temp_names)
        birthdates.append(temp_birthdates)

except FileNotFoundError:
    print(f"File called 'DOB.txt' not found")

# To print to the desired output format i used the sep paramete in print() from the link below.
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
print("Name", *names, sep ="\n")
print("\nBirthdate", *birthdates, sep = "\n")