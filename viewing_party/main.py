def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    return {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }