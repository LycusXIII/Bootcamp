'''
The following programs ask the user for the times in minutes he achieved during the triathlon
in 3 events namely swimming cycling running then calculates the total score and lets the 
the user knows which rewards the user will obtain. 
'''

# Asks the user for their times for the 3 events in the triathlon
swimming_time, cycling_time, running_time = map(float,input("Please enter the times (in minutes) the following events in order Swimming, Cycling, Running separated by a space. (e.g. 10 20 30)\n").split(" "))

# Calculates the total time and gives an output of how long it took the user to have completed the triathlon
total_time = swimming_time + cycling_time + running_time
print(f"The time it took to complete the triathlon was {total_time} minutes for the participant.")

# Based on the value from the total time the corresponding output will be shown to the user
# and the appropriate reward will be given
if total_time >= 0 and total_time <= 100:
    print("Participant is awarded Provincial Colours.")
elif total_time >= 101 and total_time <= 105:
    print("Participant is awarded Provincial Half Colours")
elif total_time >= 106 and total_time <= 110:
    print("Participant is awarded Provincial Scroll")
elif total_time > 110:
    print("Participant receives no award")
else: 
    print("Invalid time!")


# if 0 <= total_time <= 100: (never seen this in my life also their examples never showed this)

# edited code from the above with new
# if 0 >= total_time <= 100:
#     print("Participant is awarded Provincial Colours.")
# elif  101 >= total_time <= 105:
#     print("Participant is awarded Provincial Half Colours")
# elif 106 >= total_time <= 110:
#     print("Participant is awarded Provincial Scroll")
# elif total_time > 110:
#     print("Participant receives no award")