import re, os

from collections import Counter

def split_str(string):
	res = string.split(',')
	i = 0
	while i < len(res) - 1:
		field = res[i]
		if (field[0] == '"' and field[len(field) - 1] != '"'):
			j = i + 1
			while j < len(res):
				part = res[j]
				res[i] = res[i] + "," + part
				res.pop(j)
				right1 = part[len(part) - 1]
				right2 = part[len(part) - 2] 
				if (right1 == '"' or (right1 == '\n' and right2 == '"')):
					break
		i += 1
	return res

class Movies:
	"""
	Analyzing data from movies.csv
	"""
	def __init__(self, path_to_the_file):
		"""
		Put here any fields that you think you will need.
		"""
		try:
			if not os.path.isfile(path_to_the_file):
				raise Exception(f"File '{path_to_the_file}' does not exists")   
			with open(path_to_the_file, 'r') as fp:
				if fp.readline().strip() != 'movieId,title,genres':
					raise Exception()
				self.titles = {}
				self.genres = {}
				for line in fp.readlines():
					a, d, f = split_str(line.rstrip())
					d = d.strip('\"')
					self.titles[int(a)] = d.strip('\"').strip()
					self.genres[int(a)] = f.split('|')
		except Exception as e:
			raise Exception(f"File '{path_to_the_file}' is not a valid movies file")

	def dist_by_release(self):
		"""
		The method returns a dict or an OrderedDict where the keys are years and the values are counts. 
		You need to extract years from the titles. Sort it by counts descendingly.
		"""
		years = []
		for x in self.titles.values():
			m = re.search(r' \(\d\d\d\d\)$', x)
			if m:
				years.append(m.group(0)[2:6])
			else:
				years.append('N/A')
		release_years = sorted(Counter(years).items(), key=lambda x: x[1], reverse=True)
		return dict(release_years)

	def dist_by_genres(self):
		"""
		The method returns a dict where the keys are genres and the values are counts.
		Sort it by counts descendingly.
		"""
		genres_unsorted = Counter([x for each in self.genres.values() for x in each])
		genres = dict(sorted(genres_unsorted.items(), key=lambda x: x[1], reverse=True))
		return genres

	def most_genres(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and 
		the values are the number of genres of the movie. Sort it by numbers descendingly.
		"""
		movies_unsorted = {self.titles[key]: len(value) for key, value in self.genres.items()}
		movies = dict(Counter(movies_unsorted).most_common(n))
		return movies

	def get_movies_from_title(self, titles):
		"""
		The method returns a dict where the keys are movie s and values genres. Sorted by titles.
		"""
		movies_unsorted = {}
		for title in titles:
			for key, value in self.titles.items():
				if title == value:
					movies_unsorted[title] = self.genres[key]
		movies = dict(sorted(movies_unsorted.items()))
		return movies