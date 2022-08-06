import tweepy
import json
import os

#Must use Twitter API v2. Can only search for recent tweets
dir = os.listdir()
print(dir)
try:
    with open('/Users/oscarvanegeren/personal_projects/permissions.json', 'r') as f:
        account = json.load(f)
        bearer_token = account["Bearer-Token"]
    f.close()
except FileNotFoundError:
    dir = os.getcwd()
    print("File Not Found. Your working directory is: ", dir)
    exit()

client = tweepy.Client(bearer_token=bearer_token)
# Replace with your own search query
query = 'from:piersmorgan has:media'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'])

for tweet in tweets.data:
    # attachments = tweet.data['attachments']
    # print(attachments)
    print(tweet.text)
    # print(tweet.created_at)



