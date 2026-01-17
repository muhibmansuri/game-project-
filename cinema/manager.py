import random

class MovieManager:
    def __init__(self):
        self.movies = [
            {"id": 1, "title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "year": 2010, "desc": "A thief who steals corporate secrets through the use of dream-sharing technology."},
            {"id": 2, "title": "The Dark Knight", "genre": "Action", "rating": 9.0, "year": 2008, "desc": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham."},
            {"id": 3, "title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "year": 2014, "desc": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
            {"id": 4, "title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7, "year": 1999, "desc": "A computer hacker learns from mysterious rebels about the true nature of his reality."},
            {"id": 5, "title": "Pulp Fiction", "genre": "Crime", "rating": 8.9, "year": 1994, "desc": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine."},
            {"id": 6, "title": "Parasite", "genre": "Thriller", "rating": 8.6, "year": 2019, "desc": "Greed and class discrimination threaten the newly formed symbiotic relationship."},
            {"id": 7, "title": "The Prestige", "genre": "Drama", "rating": 8.5, "year": 2006, "desc": "After a tragic accident, two stage magicians in 1890s London engage in a battle to create the ultimate illusion."},
            {"id": 8, "title": "Gladiator", "genre": "Action", "rating": 8.5, "year": 2000, "desc": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family."},
            {"id": 9, "title": "Django Unchained", "genre": "Western", "rating": 8.4, "year": 2012, "desc": "With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner."},
            {"id": 10, "title": "The Wolf of Wall Street", "genre": "Biography", "rating": 8.2, "year": 2013, "desc": "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government."},
        ]

    def get_all(self):
        return self.movies

    def search(self, query):
        if not query:
            return self.movies
        query = query.lower()
        return [m for m in self.movies if query in m['title'].lower() or query in m['genre'].lower()]

    def get_recommendations(self, movie_id):
        # Simple recommendation: same genre
        base_movie = next((m for m in self.movies if m['id'] == movie_id), None)
        if not base_movie:
            return random.sample(self.movies, 3)
        
        recs = [m for m in self.movies if m['genre'] == base_movie['genre'] and m['id'] != movie_id]
        if not recs:
            return random.sample(self.movies, 3)
        return recs

cinema_mgr = MovieManager()
