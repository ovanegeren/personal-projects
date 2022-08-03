import tweepy

#Must use Twitter API v2. Can only search for recent tweets

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAOaXdwEAAAAAwaMI%2FfBpgrPs6EYXSLR6cvN2%2BSk%3D1L7lkRwGSnn7w2yxwsGPpwMzaZT9ynOBZbs52l8Q11P7uUCErY")

# Replace with your own search query
query = 'from:borisjohnson has:media'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'])

for tweet in tweets.data:
    # attachments = tweet.data['attachments']
    # print(attachments)
    print(tweet.text)
    print(tweet.created_at)



