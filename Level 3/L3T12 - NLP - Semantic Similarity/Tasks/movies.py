'''This program uses spacy to determine the next movie to watch based on
the given description in the variable watched_movie then checks for
similarities inside movies.txt and prints out the title of the movie.'''
import spacy

nlp = spacy.load('en_core_web_md')


def watch_next(watched_movie):
    '''
    Recommends a movie based on the given description.
    Args:
        movie_description: The description of the watched movie.
    Returns:
        The title of the movie that is the most similar to the watched movies
        description.
    '''
    most_similar = 0
    recommended_movie = None
    with open("movies.txt", "r", encoding="utf-8") as movies:
        for line in movies:
            # Splits at ":" and specifies that it should only split it once.
            title, description = line.strip().split(":", 1)
            # Add the movie_description to the NLP
            movie_doc = nlp(description)
            similarity_score = nlp(watched_movie).similarity(movie_doc)
            if similarity_score > most_similar:
                most_similar = similarity_score
                recommended_movie = title

    return recommended_movie


watched_movie = '''Will he save their world or destroy it?
When the Hulk becomes too dangerous for the Earth, the Illuminati trick
Hulk into a shuttle and launch him into space to a planet where the Hulk
can live in peace. Unfortunately, Hulk lands on the planet Sakaar where
he is sold into slavery and trained as a gladiator.'''

recommendation = watch_next(watched_movie)
print(f"Recommended movie to watch next: {recommendation}")
