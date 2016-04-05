from src.modules.hashtag_graph import HashtagGraph
from src.modules.tests.mock_data import MockData

class TestHashtagGraph(object):
    def init_graph_data(self):
        """
        Initializes the mock-graph data and an instance of Hashtag graph.
        """
        self.graph = HashtagGraph()
        self.mock_data = MockData()

    def test_update_timestamp_edges_map(self):
        """
        checks if the timestamp-edges map is updated correctly as expected
        """
        self.init_graph_data()
        self.graph.timestamp_edges = self.mock_data.initial_timestamp_edges
        self.graph.update_timestamp_edges_map(self.mock_data.new_list_edges, self.mock_data.new_timestamp)
        assert self.graph.timestamp_edges == self.mock_data.updated_timestamp_edges

    def test_update_graph(self):
        """
        checks if the graph is updated correctly as expected
        """
        self.init_graph_data()
        self.graph.timestamp_edges = self.mock_data.initial_timestamp_edges
        self.graph.graph = self.mock_data.initial_graph
        self.graph.update_graph(self.mock_data.new_tweet)
        assert self.graph.graph.edge == self.mock_data.updated_graph.edge and \
               self.graph.timestamp_edges == self.mock_data.updated_timestamp_edges

    def test_update_edges(self):
        """
        checks if the edges are updated correctly as expected
        """
        self.init_graph_data()
        self.graph.timestamp_edges = self.mock_data.initial_timestamp_edges
        self.graph.graph = self.mock_data.initial_graph
        self.graph.update_timestamp_edges_map(self.mock_data.new_list_edges, self.mock_data.new_timestamp)
        self.graph.update_edges(self.mock_data.new_tweet.timestamp, self.mock_data.new_list_edges)
        assert self.graph.graph.edge == self.mock_data.updated_graph.edge

    def test_get_average(self):
        """
        checks if the average degree is returned as expected
        """
        self.init_graph_data()
        self.graph.graph = self.mock_data.updated_graph
        assert self.graph.get_average() == 1.50

    def test_empty_graph_get_average(self):
        """
        checks if the average degree for an empty graph(no connections) is 0.00
        """
        self.init_graph_data()
        self.graph.graph = self.mock_data.empty_graph
        assert self.graph.get_average() == 0.00

    def test_evict_edges_outside_window_no_edges_outside_window(self):
        """
        checks if edges are evicted when no edges are outside the 60sec window - no edges should be evicted
        """
        self.init_graph_data()
        self.graph.graph = self.mock_data.initial_graph
        self.graph.update_timestamp_edges_map(self.mock_data.new_list_edges, self.mock_data.new_timestamp)
        self.graph.evict_edges_outside_window(self.mock_data.new_timestamp)
        assert self.graph.graph.number_of_edges() == self.mock_data.initial_graph.number_of_edges()

    def test_evict_edges_outside_window_new_timestamp_outside_window(self):
        """
        checks if edges are evicted when the new timestamp is outside the 60sec window  -
        edges created by new timestamp(/tweet) are not added
        """
        self.init_graph_data()
        self.graph.graph = self.mock_data.initial_graph
        self.graph.update_timestamp_edges_map(self.mock_data.new_list_edges, self.mock_data.outside_window_timestamp)
        self.graph.evict_edges_outside_window(self.mock_data.outside_window_timestamp)
        assert self.graph.graph.number_of_edges() == self.mock_data.initial_graph.number_of_edges()

    def test_evict_edges_outside_window_first_timestamp_outside_window(self):
        """
        checks if edges are evicted are evicted when first timestamp is outside the window -
        edges created by first timestamp(/tweet) are evicted
        """
        self.init_graph_data()
        self.graph.graph = self.mock_data.initial_graph
        self.graph.update_timestamp_edges_map(self.mock_data.new_list_edges, self.mock_data.new_timestamp_maximum)
        self.graph.evict_edges_outside_window(self.mock_data.new_timestamp_maximum)
        assert self.graph.graph.number_of_edges() == self.mock_data.initial_graph.number_of_edges()