favourite_movies = ["The Incredible Hulk", "Guardians of the Galaxy","Avengers: Age of Ultron", 
                    "Doctor Strange", "Thor: Love and Thunder"]

# https://www.geeksforgeeks.org/enumerate-in-python/
for count, movie in enumerate(favourite_movies, 1):
    print(f"Movie {count}: {movie}")