
import tweepy

def retrieve_top_6_tweet_ids():
    # Authenticate
    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAIZb0AEAAAAAt9yPOTYwviQytuhbpvBa9Yrkoxo%3Ds0i7OOWyTMmwGKZsmYIfaRszEw1pHFe3uqQWOaxyANEA8uep8Y')

    # Replace with your user ID (can fetch it via username lookup)
    user = client.get_user(username="kikogoncalves_")
    user_id = user.data.id

    # Fetch tweets (up to 100 recent tweets)
    tweets = client.get_users_tweets(id=user_id, max_results=100, tweet_fields=["public_metrics"])

    # Sort tweets by number of likes (or retweets)
    sorted_tweets = sorted(tweets.data, key=lambda tweet: tweet.public_metrics['like_count'], reverse=True)

    # Get top 6
    top_6 = sorted_tweets[:6]

    return [tweet.id for tweet in top_6]

if __name__ == "__main__":
    print(retrieve_top_6_tweet_ids())
