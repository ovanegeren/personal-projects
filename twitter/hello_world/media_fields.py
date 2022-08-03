import tweepy

#Must use Twitter API v2. Can only search for recent tweets

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAOaXdwEAAAAAwaMI%2FfBpgrPs6EYXSLR6cvN2%2BSk%3D1L7lkRwGSnn7w2yxwsGPpwMzaZT9ynOBZbs52l8Q11P7uUCErY")

# Replace with your own search query
# query = 'covid -is:retweet has:media'
query = 'from:borisjohnson has:media'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                     media_fields=['preview_image_url'], expansions='attachments.media_keys',
                                     max_results=100)

# Get list of media from the includes object
media = {m["media_key"]: m for m in tweets.includes['media']}

for tweet in tweets.data:
    try:
        attachments = tweet.data['attachments']
        media_keys = attachments['media_keys']
    except:
        print("Error obtaining 'attatchements' / 'media_keys'")

    print(tweet)
    print(attachments)
    print(media_keys)
    if media[media_keys[0]].preview_image_url:
        print(media[media_keys[0]].preview_image_url)
    print()
