from os import remove
from spellchecker import SpellChecker
import tweepy
import json
import re

#Must use Twitter API v2. Can only search for recent tweets
permissions_path = '/Users/oscarvanegeren/personal_projects/permissions.json'
with open(permissions_path, 'r') as f:
    account = json.load(f)
    bearer_token = account["Bearer-Token"]
f.close()

client = tweepy.Client(bearer_token=bearer_token)
spell = SpellChecker()

def clean_tweet(text):
    cleantext_1 = re.sub('http://\S+|https://\S+', '', text)
    # TODO: compres regex statements
    # TODO: filter apostrophes (names marked misspelled, ie. "Putin's")
    cleantext_2 = re.sub('#\S+', '', cleantext_1)
    cleantext_final = re.sub('#\S+', '', cleantext_2)
    return cleantext_final

def get_spelling_rate(text):
    split_text = spell.split_words(text)
    known_words = spell.known(split_text)
    unknown_words = spell.unknown(split_text)
    print("Unknown words: ", unknown_words)
    known_num = len(known_words)
    unknown_num = len(unknown_words)
    try:
        return 100 * known_num / (known_num + unknown_num)
    except ZeroDivisionError:
        print("No real words used, nothing to misspel!")
        return 100


tw_handle = input("Enter the twitter handle of the user you wish to spell-check: ")

query = 'from:' + tw_handle + ' -has:media' + ' -is:retweet'


tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'])
tw_count = 0
aggregate_sp_rate = 0

for tweet in tweets.data:
    print(tweet.text)
    cleaned_tweet = clean_tweet(tweet.text)
    sp_rate = get_spelling_rate(cleaned_tweet)
    # split_tweet = spell.split_words(cleaned_tweet)
    # known_words = spell.known(split_tweet)
    # unknown_words = spell.unknown(split_tweet)
    # print("Unknown words: ", unknown_words)
    # known_num = len(known_words)
    # unknown_num = len(unknown_words)
    # sp_rate = 100 * known_num / (known_num + unknown_num)

    tw_count+=1
    aggregate_sp_rate += sp_rate
    print(tw_handle, " has a spelling rate of: ", sp_rate, "%")

print("\nOver ", tw_count, " tweets, ", tw_handle, " has an average spelling rate of: ", (aggregate_sp_rate / tw_count))

