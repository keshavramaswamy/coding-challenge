from datetime import datetime
import itertools
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Tweet(object):
    """
    a class which stores the hashtags and timestamps, generates edges of
    """
    def __init__(self, list_hashtags, timestamp):
        self.list_hashtags = list_hashtags
        self.timestamp = self.convert_to_datetime(timestamp)

    def convert_to_datetime(self, timestamp):
        """
        :return: the timestamp as a datetime object
        """
        return datetime.strptime(timestamp, '%a %b %d %H:%M:%S +0000 %Y')

    def create_edges(self):
        """
        :return: all possible pairs of edges from the hashtag list
        """
        return [edge for edge in itertools.combinations(self.list_hashtags, 2)]
