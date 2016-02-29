import json
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from properties import BROKER, TOPIC, ACTIONID, DURATION, APPNAME, MASTER


class KafkaStream(object):
    def __init__(self):
        self.sparkConf = SparkConf()
        self.sparkConf.set("spark.driver.allowMultipleContexts", "true")

    @classmethod
    def filter_rdd(cls, rdd):
        rdd_string_json = str(rdd[1])
        if "actionId" in rdd_string_json:
            json_values = json.loads(rdd_string_json)
            action_id = json_values.get("actionId")
            if action_id == ACTIONID:
                return True
            return False
        return False

    def start_stream(self):
        spark_context = SparkContext(master=MASTER, appName=APPNAME, conf=self.sparkConf)
        stream_context = StreamingContext(spark_context, batchDuration=DURATION)
        data_stream = KafkaUtils.createDirectStream(stream_context, topics=[TOPIC],
                                                    kafkaParams={"metadata.broker.list": BROKER})
        filter_values = data_stream.filter(KafkaStream.filter_rdd)
        filter_values.pprint()
        stream_context.start()
        stream_context.awaitTermination()


if __name__ == '__main__':
    stream_kafka = KafkaStream()
    stream_kafka.start_stream()
