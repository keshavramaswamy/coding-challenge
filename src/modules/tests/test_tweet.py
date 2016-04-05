from src.modules.tests.mock_data import MockTweetData
class TestTweet(object):
    def init_get_data(self):
        """
        Initializes the mock-tweet data
        """
        self.mock_tweet = MockTweetData()

    def test_create_edges_single_hashtag(self):
        """
        checks the edges formed from a single-hashtag tweet - Should be an empty list
        """
        self.init_get_data()
        tweet = self.mock_tweet.single_hashtag_tweet
        assert tweet.create_edges() == []

    def test_create_edges_zero_hashtag(self):
        """
        checks the edges formed from a zero-hashtag tweet - Should be an empty list
        """
        self.init_get_data()
        tweet = self.mock_tweet.no_hashtag_tweet
        assert tweet.create_edges() == []

    def test_create_edges_two_or_more_hashtag(self):
        """
        checks the edges formed from a two-or-more-hashtags tweet against its expected values where all pairs of edges
        are formed from the hashtags present
        """
        self.init_get_data()
        tweet = self.mock_tweet.two_or_more_hashtags_tweet
        assert tweet.create_edges() == [('Apache', 'Spark'), ('Apache', 'Hadoop'), ('Spark', 'Hadoop')]

