import random

# Took 10 jokes from this the link below
# https://shorturl.at/DnKlY (hope this shortened url works)

def funny():
    '''
    Picks a random item from a predefined list and outputs it to the console.
    Args:
        None
    Returns:
        Random item from a list.
    '''

jokes = ["Why was 6 afraid of 7? Because 7 ate 9!","What has four wheels and flies? Garbage truck.",
        "What kind of music do the mummies listen to? Wrap music.","What lights up a stadium? A match",
        "What do you call a cold dog? A chili dog!","Which key opens a banana? Mon-key.",
        "Why did the banana go to the doctor? Because it did not peel well.",
        "What does a house wear? Address!","What did '0' say to '8'? Nice belt.",
        "What kind of water doesn't freeze? Hot water."]

# Uses the random.choice() function to randomly select a item from a list
random_joke = random.choice(jokes)
print(random_joke)