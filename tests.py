import unittest
from users import User
from admins import Admin
from movies import Movie, MOVIE_NAMES

class TestMovieLibrary(unittest.TestCase):
    def setUp(self):
        self.user = User("user1", "user1@example.com", "password", "premium")
        self.admin = Admin("admin1", "admin1@example.com", "adminpassword")
        self.movies_library = [Movie(title, "Genre", 0, "Release Date") for title in MOVIE_NAMES]

    def test_add_remove_movie(self):
        movie = self.movies_library[0]
        self.admin.add_movie(movie, self.movies_library)
        self.assertIn(movie, self.movies_library)
        self.admin.remove_movie(movie, self.movies_library)
        self.assertNotIn(movie, self.movies_library)

    def test_recommendations(self):
        # Add a subset of movies to the user's favorites list
        num_movies_to_add = min(len(self.movies_library), 5)
        for movie in self.movies_library[:num_movies_to_add]:
            self.user.add_to_favorites(movie)
        recommendations = self.user.get_recommendations()
        self.assertEqual(len(recommendations), num_movies_to_add)


def test_recommendations(self):
    # Add a subset of movies to the user's favorites list
    num_movies_to_add = min(len(self.movies_library), 3)
    for movie in self.movies_library[:num_movies_to_add]:
        self.user.add_to_favorites(movie)
    recommendations = self.user.get_recommendations()
    self.assertEqual(len(recommendations), num_movies_to_add)


if __name__ == "__main__":
    unittest.main()


