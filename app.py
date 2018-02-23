from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from tweepy.parsers import JSONParser

access_token = "184258963-sCFzbBf8zSx3e5WM0iUdxgPUoaJlSVU0YtMscA0N"
access_token_secret = "xhgUuKI0LJ3j203agTG1V3hHiLcTbF6tLJVw2JnrDosWJ"
consumer_key = "oV8DxAHsDjh7BjiELD9SLO8Id"
consumer_secret = "rFj8vA6KaQt3zuYrdzV93lrYUmvqH2Lbx4HNCs8YHn536caQtg"

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    uid = 'jokowi'
    query = 'to:' + uid
    out = api.search(q=query, parser=JSONParser(),rpp=10,count=10,tweet_mode="extended")
    print(out)
