class Admin:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def add_movie(self, movie, movie_library):
        movie_library.append(movie)
        print(f"Movie '{movie.title}' added to the movie library.")

    def remove_movie(self, movie_title, movie_library):
        for movie in movie_library:
            if movie.title == movie_title:
                movie_library.remove(movie)
                print(f"Movie '{movie_title}' removed from the movie library.")
                return
        print(f"Movie '{movie_title}' not found in the movie library.")

