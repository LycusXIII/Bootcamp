'''The program uses a class called Album and
varies list for sorting and display'''


class Album:
    '''This class represents the attributes of an album'''

    def __init__(self, albumName,  albumArtist, numberOfSongs):
        '''Initializes an object with these attributes'''
        self.albumName = albumName
        self. albumArtist = albumArtist
        self.numberOfSongs = int(numberOfSongs)

    def __str__(self):
        '''Returns each attribute of the object as a list of strings'''
        return f"{self.albumName}, {self. albumArtist}, {self.numberOfSongs}"


albums1 = [
    Album("One More Light", "Linkin Park", 10),
    Album("Meteora", "Linkin Park", 13),
    Album("Minutes to Midnight", "Linkin Park", 12),
    Album("A Thousand Suns", "Linkin Park", 15),
    Album("Living Things", "Linkin Park", 12)
]

print("\nalbums1 unsorted:")
for album in albums1:
    print(album)

# https://shorturl.at/nB6ME sort() with key argument
albums1.sort(key=lambda album: album.numberOfSongs)
print("\nalbums1 sorted with key argument:")
for album in albums1:
    print(album)

albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nalbums1 element at position 1 swapped with element at position 2:")
for album in albums1:
    print(album)

albums2 = [
    Album("Night Visions", "Imagine Dragons", 11),
    Album("Smoke + Mirrors", "Imagine Dragons", 13),
    Album("Evolve", "Imagine Dragons", 11),
    Album("Origins ", "Imagine Dragons", 12),
    Album("Loom", "Imagine Dragons", 9)
]
print("\nalbums2 print:")
for album in albums2:
    print(album)

# https://shorturl.at/6rUnE
# Making use of the extend() to copy all the albums
# from albums1 into albums2
albums2.extend(albums1)
print("\nalbums2 with albums1 albums using extend():")
for album in albums2:
    print(album)

new_albums = [
    Album("Dark Side of the Moon", "Pink Floyd", 9),
    Album("Oops!... I Did It Again", "Britney Spears", 16)
]
albums2.extend(new_albums)

albums2.sort(key=lambda album: album.albumName)
print("\nalbums2 sorted alphabetically by album name:")
for album in albums2:
    print(album)

# https://www.geeksforgeeks.org/enumerate-in-python/
# Making use of enumerate to count the index
for i, album in enumerate(albums2):
    if album.albumName == "Dark Side of the Moon":
        index = i
        # Breaking out of the loop once its found.
        break
print(f"\nAlbum name 'Dark Side of the Moon' is at index: {index} in albums2")
