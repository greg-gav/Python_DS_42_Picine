from collections import Counter
from datetime import datetime

class InvalidFileFormat(Exception):
        pass

class Ratings:
    """
    Analyzing data from ratings.csv
    """
    
    def __init__(self, path_to_ratings, path_to_movies):
        """
        Put here any fields that you think you will need.
        """
        RATINGS_HEADER = ['userId', 'movieId', 'rating', 'timestamp']
        MOVIES_HEADER = ['movieId', 'title', 'genres']
        with open(path_to_ratings, 'r') as file:
            if RATINGS_HEADER != file.readline().strip().split(","):
                raise InvalidFileFormat(f"{path_to_ratings} not a valid tags file")
            data = [line.strip().split(",") for line in file.readlines()]
            self.users = self.Users(
                ids=[x[0] for x in data],
                ratings=[x[2] for x in data],
                timestamps=[x[3] for x in data]
            )
        with open(path_to_movies, 'r') as file:
            if MOVIES_HEADER != file.readline().strip().split(","):
                raise InvalidFileFormat(f"{path_to_movies} not a valid tags file")
            movie_names = {line.strip().split(',')[0] : line.strip().split(',')[1] for line in file.readlines()}
            self.movies = self.Movies(
                ids=[x[1] for x in data],
                ratings=[x[2] for x in data],
                timestamps=[x[3] for x in data],
                names=movie_names
            )
        
    class Movies:
        def __init__(self, ids, ratings, timestamps, names=None):
            self._ids = ids
            self._ratings = ratings
            self._timestamps = timestamps
            self._names = names

        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            years = [datetime.utcfromtimestamp(int(x)).strftime('%Y') for x in self._timestamps]
            ratings_by_year = dict(sorted(Counter(years).items()))
            return ratings_by_year
        
        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
            Sort it by ratings ascendingly.
            """
            ratings_distribution = dict(sorted(Counter(self._ratings).items()))
            return ratings_distribution
        
        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            """
            top_ratings = dict(Counter(self._ids).most_common(n))
            if not self._names:
                return top_ratings
            top_movies = {}
            for k in top_ratings:
                top_movies[self._names[k]] = top_ratings[k]
            return top_movies
        
        def top_by_ratings(self, n, metric='average'):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            data_dict = {x : [] for x in self._ids}
            for i, rating in enumerate(self._ratings):
                data_dict[self._ids[i]].append(rating)
            if metric == 'average':
                for key in data_dict:
                    data_dict[key] = round(sum([float(x) for x in data_dict[key]])/len(data_dict[key]), 2)
            elif metric == 'median':
                for key in data_dict:
                    data_dict[key] = round(float(sorted(data_dict[key])[(len(data_dict[key]) - 1) // 2]), 2)
            else:
                raise ValueError(f"Unexpected argument: {metric}")
            top_ratings = dict(Counter(data_dict).most_common(n))
            if not self._names:
                return top_ratings
            top_movies = {}
            for k in top_ratings:
                top_movies[self._names[k]] = top_ratings[k]
            return top_movies
        
        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
            Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            average_dict = self.top_by_ratings(len(self._ids), metric='average')
            data_dict = {x : [] for x in self._ids}
            for i, rating in enumerate(self._ratings):
                data_dict[self._ids[i]].append(rating)
            if self._names:
                top_movies = {}
                for k in data_dict:
                    top_movies[self._names[k]] = data_dict[k]
                data_dict = top_movies
            top_variance = {}
            for key in data_dict:
                top_variance[key] = \
                    round(sum(list(map(lambda x: (float(x) - average_dict[key]) * \
                        (float(x) - average_dict[key]), data_dict[key]))), 2)
            top_variance = dict(Counter(top_variance).most_common(n))
            return top_variance

    class Users(Movies):
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
        Inherit from the class Movies. Several methods are similar to the methods from it.
        """
