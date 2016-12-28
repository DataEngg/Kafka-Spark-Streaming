Kafka Streaming-Pyspark
================
## Description

We have implemented Python Kafka Spark Streaming.

# Requirements

* ```Apache Spark``` [Download](http://spark.apache.org/downloads.html)
* ```Apache Hadoop```[Donwload](https://archive.apache.org/dist/hadoop/common/hadoop-2.6.0/)

# Note

* Download Apache Spark version number 1.6.0 with Hadoop version 2.6.0.
* Download Apache Hadoop version number 2.6.0.
* After Downloading Apache Spark and Hadoop, put both of them in the Environment variable of the System.

# Running

* Before running Pyspark Kafka Streamer in a server. Run the following command

```bash

$ start-all.sh
$ cd spark-1.6.0-bin-hadoop2.6
$ ./sbin/start-master.sh
$ ./sbin/start-slaves.sh <Spark Master URL>
```

* Run the following command to run Pyspark Kafka Streamer

``` bash

$  bin/spark-submit --master <SPARK MASTER URL> --jars <PATH TO JAR>spark-streaming-kafka_2.10-1.6.0.jar
        ,<PATH TO JAR>spark-streaming-kafka-assembly_2.10-1.6.0.jar,<PATH TO JAR>/spark-streaming_2.10-1.6.0.jar
        ,<PATH TO JAR>/spark-core_2.10-1.6.0.jar,<PATH TO JAR>/kafka_2.10-0.9.0.0.jar
        Kafka-Streaming-Pyspark/kafka-stream/kafka_stream.py localhost 9999
```
# Note

* Jar are present in the lib folder and if you have different version then please download it from Maven remote
repositories.
