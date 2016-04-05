import json
from src.modules.tweet import Tweet
from src.modules.hashtag_graph import HashtagGraph
import argparse
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_tweet(json_data):
    """
    :return: Tweet object containing the list of unique hashtags and timestamp
    """
    timestamp = json_data['created_at']
    set_hashtags = {hashtag['text'] for hashtag in json_data['entities']['hashtags']}
    return Tweet(list(set_hashtags), timestamp)


def check_rate_limit_tweet(json_data):
    """
    check if the tweet has rate limit message or not
    :param json_data:
    :return: Boolean value
    """
    return 'limit' not in json_data


def analyze_tweets(input_filename, output_filename):
    """
    driver method which reads from input, creates twitter hashtag graph and writes the rolling
    average to an output file.
    :param input_filename: input file which stores the tweets
    :param output_filename: output file for storing the rolling average
    """
    try:
        with open(input_filename) as input:
            logger.info("Reading input file")
            graph = HashtagGraph()
            for line in input:
                json_data = json.loads(line)
                if check_rate_limit_tweet(json_data):
                    tweet = get_tweet(json_data)
                    graph.update_graph(tweet)
                    average_degree = graph.get_average()
                    with open(output_filename, 'a') as output:
                        output.write('%.2f\n' % average_degree)
        input.close()
        logger.info('Output written to %s', output_filename)
    except IOError:
        logger.exception('Failed to open file')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze hashtags and create hashtag graph'
                                                 'to return rolling average degree')
    parser.add_argument('input_filename', nargs='?',
                        default="./tweet_input/tweets.txt")
    parser.add_argument('output_filename', nargs='?',
                        default="./tweet_output/output.txt")
    args = parser.parse_args()
    analyze_tweets(args.input_filename, args.output_filename)
