import datetime
from src.modules.tweet import Tweet
import networkx as nx


class MockData(object):
    """
    A mockup class used to create mockup graph data required for unit testing
    """
    def __init__(self):
        self.new_timestamp = datetime.datetime(2016, 3, 24, 17, 51, 12)
        self.outside_window_timestamp = datetime.datetime(2016, 3, 24, 17, 50, 8)
        self.new_timestamp_maximum = datetime.datetime(2016, 3, 24, 17, 52, 2)

        self.new_list_edges = [('Hadoop', 'Storm')]
        self.new_tweet = Tweet(['Hadoop', 'Storm'], 'Thu Mar 24 17:51:12 +0000 2016')

        self.initial_list_edges = [('Apache', 'Spark'), ('Apache', 'Hadoop')]
        self.initial_graph = self.create_graph_edges(self.initial_list_edges)
        self.initial_timestamp_edges = {
            datetime.datetime(2016, 3, 24, 17, 51, 10): [[('Apache', 'Spark')]],
            datetime.datetime(2016, 3, 24, 17, 51, 12): [[('Apache', 'Hadoop')]]
        }

        self.updated_graph = self.create_graph_edges([('Apache', 'Spark'), ('Apache', 'Hadoop'), ('Hadoop', 'Storm')])
        self.updated_timestamp_edges = {
            datetime.datetime(2016, 3, 24, 17, 51, 10): [[('Apache', 'Spark')]],
            datetime.datetime(2016, 3, 24, 17, 51, 12): [[('Apache', 'Hadoop'), ('Hadoop', 'Storm')]]
        }

        self.empty_graph = self.create_graph_edges([])

    def create_graph_edges(self, list_edges):
        """
        returns the graph after adding the list of edges to it
        :param list_edges:
        :return: updated graph
        """
        graph = nx.Graph()
        graph.add_edges_from(list_edges)
        return graph


class MockTweetData(object):
    """
    A mockup class used to create mockup tweet data required for unit testing
    """
    def __init__(self):
        self.timestamp = datetime.datetime(2016, 3, 24, 17, 51, 12)
        self.list_hashtags = ['Hadoop', 'Storm']
        self.json_data = {"created_at": 'Thu Mar 24 17:51:12 +0000 2016',
                          "entities": {"hashtags": [{"text": "Hadoop"}, {"text": "Storm"}]}}
        self.rate_limit = {"limit": {"track": 5, "timestamp_ms":"1446218985743"}}
        self.single_hashtag_tweet = Tweet(['Hadoop'], 'Thu Mar 24 17:51:12 +0000 2016')
        self.no_hashtag_tweet = Tweet([], 'Thu Mar 24 17:51:12 +0000 2016')
        self.two_or_more_hashtags_tweet = Tweet(['Apache', 'Spark', 'Hadoop'], 'Thu Mar 24 17:51:12 +0000 2016')

