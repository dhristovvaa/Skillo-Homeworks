class User:
    def __init__(self, username, email, password, subscription_type):
        self.username = username
        self.email = email
        self.password = password
        self.subscription_type = subscription_type
        self.favorites_list = []
        self.watched_list = []

    def add_to_favorites(self, movie):
        self.favorites_list.append(movie)

    def mark_as_watched(self, movie):
        self.watched_list.append(movie)

    def rate_movie(self, movie, rating):
        if 1 <= rating <= 5:
            movie.rating = rating
        else:
            print("Rating should be between 1 and 5.")

    def get_recommendations(self):
        if len(self.favorites_list) >= 3:
            return self.favorites_list[-3:]
        else:
            return self.favorites_list

    def get_watched_list(self):
        return self.watched_list
