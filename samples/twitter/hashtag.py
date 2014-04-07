import sys
import time
import random
import logging
import datetime
from twitter import *
from petrel import storm
from petrel.emitter import Spout

log = logging.getLogger('hashtagspout')

log.debug('hashtagspout started')

class HashtagSpout(Spout):
	def __init__(self):
		super(HashtagSpout, self).__init__(script=__file__)

	def declareOutputFields(cls):
		return ['tag', 'date']

	t = [
	[{'indices': [96, 101], 'text': 'cute'}],
	[{'indices': [96, 101], 'text': 'beauty'}],
	[{'indices': [96, 101], 'text': 'nice'}]
	]

	def nextTuple(self):
		tag = self.t[random.randint(0, len(self.t) - 1)]
		date = datetime.datetime.now()
		log.debug('hashtagspout emitting: %s', tag)
		storm.emit([tag, date])

def run():
	HashtagSpout().run()