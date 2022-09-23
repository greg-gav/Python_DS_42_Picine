from collections import Counter

class InvalidFileFormat(Exception):
        pass

class Tags:
    """
    Analyzing data from tags.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        VALID_HEADER = ['userId', 'movieId', 'tag', 'timestamp']
        with open(path_to_the_file, 'r') as file:
            if VALID_HEADER != file.readline().strip().split(","):
                raise InvalidFileFormat(f"{path_to_the_file} not a valid tags file")
            self._tag_list = [line.split(",")[2].strip() for line in file.readlines()]                

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
        where the keys are tags and the values are the number of words inside the tag.
        Drop the duplicates. Sort it by numbers descendingly.
        """
        sorted_tags = sorted(set(self._tag_list), key=lambda x: len(x.split()), reverse=True)
        big_tags = {sorted_tags[n]: len(sorted_tags[n].split()) for n in range(n)}
        return big_tags

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = sorted(set(self._tag_list), key=lambda x: len(x), reverse=True)[:n]
        return big_tags

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        big_tags = list(set(self.most_words(n).keys()) & set(self.longest(n)))
        return big_tags
        
    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        popular_tags = dict(Counter(self._tag_list).most_common(n))
        return popular_tags

    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        tags_with_word = sorted(filter(lambda x: word.lower() in x.lower().split(), set(self._tag_list)))
        return tags_with_word
