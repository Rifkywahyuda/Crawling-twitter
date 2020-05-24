import sys
from tweepy.streaming import StreamListener
from tweepy import Stream
import tweepy

#Variables that contains the credentials to access Twitter API
access_token = '604171117-8xplKPf2RmZSnCZ8M0Jw3ojkRFqnYgn2dSQkDJG4'
access_secret = 'D6KjFzBUn4BCfAGSjpmihezUtJAtpouGYOopWk1Q2CDdS'
consumer_key = 'eeolPDcxsy3TFcd1kiHcH8xQi'
consumer_secret = 'bEoiMK181HniqDJgQGHV2l2uH2aWeM0Ma3lp8pVNgLxrFXT0aO'

class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    
    stream.filter(track=['python', 'javascript', 'ruby'])
