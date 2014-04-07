import sys
import logging
import datetime
from petrel import storm
from petrel.emitter import BasicBolt

log = logging.getLogger('splithashtag')
log.debug('splithashtag Started')

class SplitHashtagBolt(BasicBolt):
	def __init__(self):
		super(SplitHashtagBolt, self).__init__(script=__file__)

	@classmethod
	def declareOutputFields(self):
		return ['tag', 'date']

	def process(self, tup):
		log.debug('SplitHashtagBolt.process() started with: %s', tup)
		t = tup.values[0]
		if t.has_key('entities'):
			if t['entities']['hashtags']:
				for i in t['entities']['hashtags']:
					try:
						tag = str(i['text'].decode("ascii"))
						date = t['created_at']
						storm.emit([tag, date])
					except:
						tag = "None"
						date = "None"
						storm.emit([tag, date])
			else:
				tag = "None"
				date = "None"
				storm.emit([tag, date])
		else:
			tag = "None"
			date = "None"
			storm.emit([tag, date])			


def run():
	SplitHashtagBolt().run()