import networkx as nx
import datetime
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HashtagGraph(object):
    """
    a class which updates the graph and calculates its average degree
    """
    def __init__(self):
        self.graph = nx.Graph()
        self.timestamp_edges = {}

    def update_graph(self, tweet):
        """
        updates the edges in the graph by processing the tweet and checking the 60 sec window
        :param tweet: latest tweet object read
        """
        list_edges = tweet.create_edges()
        if list_edges:
            self.update_timestamp_edges_map(list_edges, tweet.timestamp)
            self.update_edges(tweet.timestamp, list_edges)

    def update_timestamp_edges_map(self, list_edges, timestamp):
        """
        updates the timestamp_edges map with every incoming list_edges and timestamp
        :param list_edges: list of new edges created from latest tweet
        :param timestamp: timestamp of latest tweet
        """
        if timestamp not in self.timestamp_edges:
            self.timestamp_edges[timestamp] = list()
            self.timestamp_edges[timestamp].append(list_edges)
        else:
            self.timestamp_edges[timestamp][0].extend(list_edges)

    def evict_edges_outside_window(self, new_timestamp):
        """
        removes edges outside the 60 second window of the maximum timestamp processed (or being processed)
        :param timestamp: the latest timestamp processed
        """
        max_timestamp = max(self.timestamp_edges)
        limit = max_timestamp - datetime.timedelta(seconds=60)
        for timestamp in self.timestamp_edges.keys():
            if timestamp <= limit:
                if timestamp != new_timestamp:
                    remove_edges = self.timestamp_edges[timestamp][0]
                    self.graph.remove_edges_from(remove_edges)
                del self.timestamp_edges[timestamp]

    def update_edges(self, timestamp, list_edges):
        """
        updates the edges of the graph with the latest produced edges
        :param timestamp: timestamp of latest tweet
        :param list_edges: edges of latest tweet
        """
        new_timestamp = timestamp
        self.evict_edges_outside_window(timestamp)
        if new_timestamp in self.timestamp_edges:
            self.graph.add_edges_from(list_edges)

    def get_average(self):
        """
        calculates the average degree of the graph
        :return: the average degree of the graph
        """
        number_of_nodes = len(self.graph)
        if number_of_nodes:
            return (2 * self.graph.size())/float(number_of_nodes)
        else:
            return 0.00

