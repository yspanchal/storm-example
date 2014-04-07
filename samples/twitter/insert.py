import redis
from twitter import *


auth = OAuth(
    consumer_key="************************",
    consumer_secret="******************************",
    token="****************************************",
    token_secret="**************************************"
)

r = redis.StrictRedis(host='localhost', port=6379, db=0)
t = TwitterStream(auth=auth, domain='stream.twitter.com').statuses.sample()

for i in t:
	r.rpush("hashtags", i)
