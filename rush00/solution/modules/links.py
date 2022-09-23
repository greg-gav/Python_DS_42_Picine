import requests, os, datetime

from bs4 import BeautifulSoup
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

def readfile(path_to_the_file, header):
	if not os.path.isfile(path_to_the_file):
		raise Exception(f"File '{path_to_the_file}' does not exists")   
	try:
		with open(path_to_the_file, 'r') as fp:
			if fp.readline().strip() != header:
				raise Exception()
			first = {}
			second = {}
			for x in fp.readlines():
				a, b, c = split_str(x.rstrip())
				b = b.strip('\"')
				first[int(a)] = b
				second[int(a)] = c
	except Exception as e:
		raise Exception(f"File '{path_to_the_file}' is not a valid links file")
	return first, second

class Links:
	"""
	Analyzing data from links.csv
	"""
	def __init__(self, path_to_the_file_links, path_to_the_file_movies):
		"""
		Put here any fields that you think you will need.
		"""    
		self.imdbId, self.tmdbId = readfile(path_to_the_file_links, 'movieId,imdbId,tmdbId')
		self.titles, self.genres = readfile(path_to_the_file_movies, 'movieId,title,genres')

	def get_imdb(self, list_of_movies, list_of_fields = ['Director', 'Budget', 'Cumulative Worldwide Gross', 'Runtime']):
		"""
		The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
			For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
			The values should be parsed from the IMDB webpages of the movies.
		Sort it by movieId descendingly.
		"""
		imdb_info = []
		for each in list_of_movies:
			response = requests.get('https://www.imdb.com/title/tt' + self.imdbId[each] + '/')
			if response.status_code != 200:
				raise Exception("URL does not exist")
			soup = BeautifulSoup(response.content, 'html.parser')
			res = [each]
			for field in list_of_fields:
				if field == 'Cumulative Worldwide Gross':
					field = 'Gross worldwide'
				elif field == 'Director':
					field = ['Director', 'Directors']
				tag = soup.find(string=field)
				if tag != None:
					if tag.next_element.string == None: 
						if 'Runtime' in field:
							timestr = "".join([x.string.strip()[0:4] for x in tag.next_element.children])
							date_time_obj = datetime.datetime.strptime(timestr, '%Hhour%Mminu')
							res.append(str(date_time_obj.time()))
						else:
							res.append('N/A')
					else:
						if field in ['Budget', 'Gross worldwide']:
							numstr = tag.next_element.string.split(' ')[0]
							numstr = numstr.replace('$', '')
							numstr = numstr.replace(',', '')
							res.append(numstr)
						else:
							res.append(tag.next_element.string)
				else:
					res.append('N/A')
			imdb_info.append(res)
		imdb_info.sort(reverse = True, key=lambda x: x[0])
		return imdb_info
		
	def top_directors(self, n):
		"""
		The method returns a dict with top-n directors where the keys are directors and 
		the values are numbers of movies created by them. Sort it by numbers descendingly.
		"""
		info = self.get_imdb(list(range(1,11)), ['Director'])
		directors_unsorted = Counter([each[1] for each in info])
		directors = dict(Counter(directors_unsorted).most_common(n))
		return directors
		
	def most_expensive(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are their budgets. Sort it by budgets descendingly.
		"""
		info = self.get_imdb(list(range(1,11)), ['Budget'])
		budgets_unsorted = {}
		for each in info:
			if each[1] != 'N/A':
				budgets_unsorted[self.titles[each[0]]] = int(each[1])
		budgets = dict(sorted(budgets_unsorted.items(), key=lambda x: x[1], reverse=True)[0:n])
		return budgets
		
	def most_profitable(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are the difference between cumulative worldwide gross and budget.
		Sort it by the difference descendingly.
		"""
		info = self.get_imdb(list(range(1,11)), ['Budget', 'Cumulative Worldwide Gross'])
		profits_unsorted = {self.titles[each[0]]: int(each[2]) - int(each[1]) for each in info 
			if each[1] != 'N/A' and each[2] != 'N/A' }
		profits = dict(sorted(profits_unsorted.items(), key=lambda x: x[1], reverse=True)[0:n])
		return profits
		
	def longest(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
		the values are their runtime. If there are more than one version – choose any.
		Sort it by runtime descendingly.
		"""
		info = self.get_imdb(list(range(1,11)), ['Runtime'])
		runtimes_unsorted = {}
		for each in info:
			if each[1] != 'N/A':
				time = datetime.datetime.strptime(each[1], '%H:%M:%S')
				runtimes_unsorted[self.titles[each[0]]] = str(time.time())
		runtimes = dict(sorted(runtimes_unsorted.items(), key=lambda x: x[1], reverse=True)[0:n])
		return runtimes
		
	def top_cost_per_minute(self, n):
		"""
		The method returns a dict with top-n movies where the keys are movie titles and
	the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it. 
		The values should be rounded to 2 decimals. Sort it by the division descendingly.
		"""
		info = self.get_imdb(list(range(1,11)), ['Budget', 'Runtime'])
		costs_unsorted = {}
		for each in info:
			if each[1] != 'N/A' and each[2] != 'N/A':
				time = datetime.datetime.strptime(each[2], '%H:%M:%S')
				costs_unsorted[self.titles[each[0]]] = float(each[1]) / (time.time().hour * 60  + time.time().minute)
		costs = dict(sorted(costs_unsorted.items(), key=lambda x: x[1], reverse=True)[0:n])
		return costs
