import pytest

@pytest.fixture(scope='session')
def analytics_instance():
    from movielens_analysis import Analytics
    return Analytics('ml-latest-small')

@pytest.fixture(scope='session')
def tags_instance():
    from modules.tags import Tags
    return Tags('ml-latest-small/tags.csv')

@pytest.fixture(scope='session')
def links_instance():
    from modules.links import Links
    return Links('ml-latest-small/links.csv', 'ml-latest-small/movies.csv')

@pytest.fixture(scope='session')
def movies_instance():
    from modules.movies import Movies
    return Movies('ml-latest-small/movies.csv')

@pytest.fixture(
    scope='session',
    params=['movies_instance', 'users_instance']
)
def get_instance(request):
    from modules.ratings import Ratings
    if request.param == 'movies_instance':
        return Ratings('ml-latest-small/ratings.csv', 'ml-latest-small/movies.csv').movies
    else:
        return Ratings('ml-latest-small/ratings.csv', 'ml-latest-small/movies.csv').users

@pytest.fixture(
    scope='function',
    params=[0,1,10,20,50,100,200]
)
def number(request):
    return request.param
