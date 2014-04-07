import twitterfeed
import splithashtag
import hashtagcount

def create(builder):
	builder.setSpout("spout", twitterfeed.HashtagSpout(), 1)
	builder.setBolt("split", splithashtag.SplitHashtagBolt(), 1).shuffleGrouping("spout")
	builder.setBolt("count", hashtagcount.HashtagCountBolt(), 1).fieldsGrouping("split", ["tag"])