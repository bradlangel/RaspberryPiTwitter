# This script will pull a feed from Twitter from the users unblocked users.
# Blocking a user in Twitter will not pull their tweets.

from feedrenderer import *
from twitterrepository import *

# You must register your own application and fill in the following fields.
# https://dev.twitter.com/docs/auth/tokens-devtwittercom
consumerKey = 'y9h2wiSBqvAg8xwhu67KA'
consumerSecret = 'aQSis1UMnwZjTWPNxt5zglyuZZKqiNeDT85c4O2vTE'
apiKey = '39705383-1tAeEMpeWe1DXTWVOaYaWuHR3CCy7cQMCJ5GCJMub'
apiSecret = 'emv9SrFa71OVP8videz8sbsvOqLldYri6hwgqtUb4YLv0'

renderer = FeedRenderer(2, 2)

twitterRepository = TwitterRepository(consumerKey, consumerSecret, apiKey, apiSecret)

def Draw():
    tweets = twitterRepository.GetTweetsFromUnblockedUsers('from:StartupInst', 4)
    renderer.DrawFeed(tweets)
    renderer.root.after(1000, Draw)

Draw()
renderer.Draw()
