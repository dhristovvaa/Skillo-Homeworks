

from users import User
from admins import Admin
from movies import Movie, MOVIE_NAMES

# Create movie instances
movies_library = [Movie(title, "Genre", 0, "Release Date") for title in MOVIE_NAMES]

# Create a user
user1 = User("user1", "user1@example.com", "password", "premium")

# Add movies to favorites
for movie in movies_library:
    user1.add_to_favorites(movie)

# Get recommendations
recommendations = user1.get_recommendations()
print("Recommended movies:")
for movie in recommendations:
    print(movie.title)

# Mark movies as watched and rate them
for movie in recommendations:
    user1.mark_as_watched(movie)
    user1.rate_movie(movie, 4)

# Get watched list
watched_list = user1.get_watched_list()
print("\nWatched movies:")
for movie in watched_list:
    print(movie.title, "- Rating:", movie.rating)

