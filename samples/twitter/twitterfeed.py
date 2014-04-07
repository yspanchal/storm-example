import sys
import time
import redis
import random
import logging
import datetime
from petrel import storm
from petrel.emitter import Spout

log = logging.getLogger('hashtagspout')

log.debug('hashtagspout started')

class HashtagSpout(Spout):
	def __init__(self):
		super(HashtagSpout, self).__init__(script=__file__)

	@classmethod
	def declareOutputFields(cls):
		return ['tag']

	r = redis.StrictRedis(host='localhost', port=6379, db=0)

	def nextTuple(self):
		time.sleep(5)
		tag = eval(self.r.lpop("hashtags"))
		log.debug('hashtagspout emitting: %s', tag)
		storm.emit([tag])

def run():
	HashtagSpout().run()