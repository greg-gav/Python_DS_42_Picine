from modules.links import Links
from modules.movies import Movies
from modules.ratings import Ratings
from modules.tags import Tags
	
class Analytics:
	def __init__(self, dir_path):
		try:
			self.links = Links(dir_path + '/links.csv', dir_path + '/movies.csv')
			self.movies = Movies(dir_path + '/movies.csv')
			self.tags = Tags(dir_path + '/tags.csv')
			self.ratings = Ratings((dir_path + '/ratings.csv'), (dir_path + '/movies.csv'))
		except Exception as e:
			raise e
	
	def dict_to_int(self, d):
		return { key : int(value) for key, value in d.items() }