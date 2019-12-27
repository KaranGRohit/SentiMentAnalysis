import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler
import twitter_credentials

class StdOutListener(StreamListener):

    def self_data(self, data):
        print(data)
        return true

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_SECRET)

    stream = Stream(auth, listener)
    stream.filter(track=['donald trump','hillary clinton','barack obama','bernie sanders'])
