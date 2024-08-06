'''This program reads and XML and displays the requested information'''

import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

# Loops through each of the 'movie' elements
for child in root.iter('movie'):
    print(child.tag, child.attrib)

# Loops through each 'movie' element inside "genre/decade/movie"
for movie in root.findall("genre/decade/movie"):
    description = movie.find("description")
    if description is not None:
        print(''.join(description.itertext()))

favorite_count = 0
# Loops through each 'movie' element where the child favorite = True
for movie in root.findall('.//movie[@favorite="True"]'):
    favorite_count += 1
print(f"Total favorite movies: {favorite_count}")

disliked_count = 0
# Loops through each 'movie' element where the child favorite = False
for movie in root.findall('.//movie[@favorite="False"]'):
    disliked_count += 1
print(f"Total disliked movies: {disliked_count}")

# https://docs.python.org/3/library/xml.etree.elementtree.html
# https://www.w3schools.com/xml/xpath_syntax.asp
