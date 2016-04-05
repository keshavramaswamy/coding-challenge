from src.modules.tests.mock_data import MockTweetData
from src.modules.twitter_hashtag_graph_analyzer import check_rate_limit_tweet
from src.modules.twitter_hashtag_graph_analyzer import get_tweet


class TestTwitterHashtagGraphAnalyzer(object):
    def init_get_data(self):
        """
        Initializes the mock-tweet data
        """
        self.mock_tweet_data = MockTweetData()

    def test_get_tweet(self):
        """
        checks if the Tweet instance obtained from the mock-tweet data is of expected value
        """
        self.init_get_data()
        tweet_json_data = self.mock_tweet_data.json_data
        tweet = get_tweet(tweet_json_data)
        assert tweet.timestamp == self.mock_tweet_data.timestamp and \
               tweet.list_hashtags == self.mock_tweet_data.list_hashtags

    def test_check_no_rate_limit_json_tweet_data(self):
        """
        checks if there is rate limit in the json data containing no rate limit - should return True
        """
        self.init_get_data()
        tweet_json_data = self.mock_tweet_data.json_data
        no_check_rate_limit = check_rate_limit_tweet(tweet_json_data)
        assert no_check_rate_limit is True

    def test_check_no_rate_limit(self):
        """
        checks if there is rate limit in the json data containing rate limit - should return False
        """
        self.init_get_data()
        tweet_json_data = self.mock_tweet_data.rate_limit
        no_check_rate_limit = check_rate_limit_tweet(tweet_json_data)
        assert no_check_rate_limit is False

