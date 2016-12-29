#pip install tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "tZRi2DVFSeEl4K77R2yNLE8aQ"
access_token_secret = "Wnewl8PFjgBC9QlIimLpirYvdPvrvE9Mx4vEOeCvFPeuQr9s5G"
consumer_key ='2341848095-rFwC9RZJceJGUvAsTEUivc8Hq6mdaHBGoFlNo44'
consumer_secret = 'xFCaYxcGjN2X4aVCXu3cV0U8spIAiiVgwabygVfFkmIbU'


class StdOutListener(StreamListener):
    """A basic listener that just prints received tweets to stdout."""
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(track=['python', 'datamining', 'hashing'])
