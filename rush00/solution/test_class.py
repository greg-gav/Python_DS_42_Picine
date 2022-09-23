import pytest
from collections import OrderedDict

class Tests:

    @pytest.mark.parametrize(
            "d",
            (
                {'str': float(21.21)} , {'str1': float(21.21), 'str2': float(42.42)},
            )
        )
    def test_dict_to_int(self, analytics_instance, d):
        result = analytics_instance.dict_to_int(d)
        assert isinstance(result, dict)
        assert all(isinstance(x, int) for x in result.values())

    class TestTags:

        def test_tags_most_words(self, tags_instance, number):
            result = tags_instance.most_words(number)
            assert isinstance(result, dict)
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)

        def test_tags_longest(self, tags_instance, number):
            result = tags_instance.longest(number)
            assert isinstance(result, list)
            assert all(isinstance(x, str) for x in result)
            assert result == sorted(result, key=lambda x: len(x), reverse=True)

        def test_tags_most_words_and_longest(self, tags_instance, number):
            result = tags_instance.most_words_and_longest(number)
            assert isinstance(result, list)
            assert all(isinstance(x, str) for x in result)

        def test_tags_most_popular(self, tags_instance, number):
            result = tags_instance.most_popular(number)
            assert isinstance(result, dict)
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)

        @pytest.mark.parametrize(
            "word",
            ('bob', 'horror', 'none', 'amazing', 'cool')
        )
        def test_tags_most_tags_with(self, tags_instance, word):
            result = tags_instance.tags_with(word)
            assert isinstance(result, list)
            assert all(isinstance(x, str) for x in result)
            assert result == sorted(result)
    

    class TestRatings:
            
        def test_movies_dist_by_year(self, get_instance):
            result = get_instance.dist_by_year()
            assert isinstance(result, dict)
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.keys()) == sorted(result.keys())

        def test_movies_dist_by_rating(self, get_instance):
            result = get_instance.dist_by_rating()
            assert isinstance(result, dict)
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.keys()) == sorted(result.keys())

        def test_movies_top_by_num_of_ratings(self, get_instance, number):
            result = get_instance.top_by_num_of_ratings(number)
            assert isinstance(result, dict)
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)
    
        @pytest.mark.parametrize(
            "metric",
            ('average', 'median')
        )
        def test_movies_top_by_ratings(self, get_instance, number, metric):
            result = get_instance.top_by_ratings(number, metric)
            assert isinstance(result, dict)
            assert all(isinstance(x, float) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)

        @pytest.mark.parametrize(
            "metric",
            ('', 'none', 'wrong')
        )
        def test_movies_top_by_ratings_wrong(self, get_instance, number, metric):
            with pytest.raises(ValueError):
                get_instance.top_by_ratings(number, metric)

        def test_top_controversial(self, get_instance, number):
            result = get_instance.top_by_ratings(number)
            assert isinstance(result, dict)
            assert all(isinstance(x, float) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)

    class TestLinks:
        @pytest.mark.parametrize(
            "movie_id",
            (
                [141],
                [1456, 207],
                [1257, 1268, 782],
                [5212, 5048, 5507, 7789],
                [145745, 55112, 4723, 2396, 159093],
            )
        )
        def test_get_imdb(self, links_instance, movie_id):
            result = links_instance.get_imdb(movie_id)
            assert isinstance(result, list)
            assert all(isinstance(x, list) for x in result)
            assert result == sorted(result, key=lambda x: x[0], reverse=True)
		
        @pytest.mark.parametrize( "n", (1, 3, 5, ) )
        def test_top_directors(self, links_instance, n):
            result = links_instance.top_directors(n)
            assert isinstance(result, dict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)
            assert len(result) == n

        @pytest.mark.parametrize( "n", (1, 3, 5, ) )
        def test_most_expensive(self, links_instance, n):
            result = links_instance.most_expensive(n)
            assert isinstance(result, dict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)
            assert len(result) == n

        @pytest.mark.parametrize( "n", (1, 3, 5, ) )
        def test_most_profitable(self, links_instance, n):
            result = links_instance.most_profitable(n)
            assert isinstance(result, dict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)
            assert len(result) == n

        @pytest.mark.parametrize( "n", (1, 3, 5, ) )
        def test_longest(self, links_instance, n):
            result = links_instance.longest(n)
            assert isinstance(result, dict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, str) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)
            assert len(result) == n

        @pytest.mark.parametrize( "n", (1, 3, 5, ) )
        def test_top_cost_per_minute(self, links_instance, n):
            result = links_instance.top_cost_per_minute(n)
            assert isinstance(result, dict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, float) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)		
            assert len(result) == n

    class TestMovies:

        def test_dist_by_release(self, movies_instance):
            result = movies_instance.dist_by_release()
            assert isinstance(result, dict) or isinstance(result, OrderedDict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)	

        def test_dist_by_genres(self, movies_instance):
            result = movies_instance.dist_by_genres()
            assert isinstance(result, dict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)	

        @pytest.mark.parametrize( "n", (1, 10, 50, ) )
        def test_most_genres(self, movies_instance, n):
            result = movies_instance.most_genres(n)
            assert isinstance(result, dict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, int) for x in result.values())
            assert list(result.values()) == sorted(result.values(), reverse=True)	
            assert len(result) == n

        @pytest.mark.parametrize(
            "movie_title",
            (
                ['Rubber (2010)'], ['Rubber (2010)', 'Mulan (1998)'],
            )
        )
        def test_get_movies_from_title(self, movies_instance, movie_title):
            result = movies_instance.get_movies_from_title(movie_title)
            assert isinstance(result, dict)
            assert all(isinstance(x, str) for x in result.keys())
            assert all(isinstance(x, list) for x in result.values())
            assert list(result.keys()) == sorted(result.keys())	
