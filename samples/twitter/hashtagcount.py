import sys
import MySQLdb
import logging
import calendar
from dateutil.parser import parse
from collections import defaultdict
from petrel import storm
from datetime import datetime
from petrel.emitter import BasicBolt

log = logging.getLogger('hashtagcount')
log.debug('hashtagcount started')

class HashtagCountBolt(BasicBolt):
	def __init__(self):
		super(HashtagCountBolt, self).__init__(script=__file__)
		self._count = defaultdict(int)

	@classmethod
	def declareOutputFields(cls):
		return ['tag', 'count', 'date']

	def process(self, tup):
		log.debug("HashtagCountBolt.process() started with: %s", tup)
		tag = tup.values[0]
		if tag != "None":
			self._count[tag] += 1
			d = parse(tup.values[1])
			date = calendar.timegm(d.timetuple())
			db = MySQLdb.connect("localhost","root","password","twitter")
			cursor = db.cursor()
			sql = """INSERT INTO hashtags (hashtag, datetime, count) values ('%s', '%s', %d) on duplicate key update count=%d""" % (tag, date, self._count[tag], self._count[tag])
			cursor.execute(sql)
			db.commit()
			storm.emit([tag, self._count[tag], date])
		else:
			storm.emit(["None", "None", "None"])

def run():
	HashtagCountBolt().run()
