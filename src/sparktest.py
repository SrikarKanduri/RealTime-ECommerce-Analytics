import sys

import os

import shutil

import re



from pyspark import SparkContext, SparkConf

from pyspark.streaming import StreamingContext

from pyspark.streaming.kafka import KafkaUtils

from pymongo import MongoClient

from kafka import KafkaProducer 



# client = MongoClient('localhost', 27017)



# db = client.output_db

# averages = db.averages



producer = KafkaProducer(bootstrap_servers=['152.46.16.76:9092'])







def decoder(msg):

    return msg



if(os.path.exists("./counts")):

    shutil.rmtree("./counts")



conf = SparkConf().setAppName("Spark Application")

sc = SparkContext.getOrCreate()

sc.setLogLevel("WARN")



ssc = StreamingContext(sc, 10)



kafkaStream = KafkaUtils.createDirectStream(ssc, ['testtopic'],{"bootstrap.servers": "152.46.16.76:9092"})



offsetRanges = []



def storeOffsetRanges(rdd):

    global offsetRanges

    offsetRanges = rdd.offsetRanges()

    return rdd



def printOffsetRanges(rdd):

    for o in offsetRanges:

        print(o)

        print "%s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset)



def publish(line):

    records = line.collect()

    for record in records:

        rec = {

            "name": str(record[0]),

            "sum": str(record[1][0]),

            "count": str(record[1][1]),

            "state": str(record[1][2]),

            "cname": str(record[1][3]),

            "month": str(record[1][4])

        }

        print(rec)

        producer.send('outputtopic', str(rec))





def split(line):

    line = line[1:-1]

    res = line.split(", ")

    fin = ""

    pname = None

    rating = None

    state = None

    cname = None

    month = None

    for r in res:

        left, right = r.split("=")

        if left == "pname":

            pname = right

        

        if left == "rating":

            rating = right



        if left == "state":

            state = right



        if left == "cname":

            cname = right



        if left == "purchase_month":

            month = right



    return [pname + " : " + rating + " : " + state + " : " + cname + " : " + month]



def mapper(word):

    pname, rating, state, cname, month = word.split(" : ")

    return (pname, (float(rating), 1, state, cname,month))



def reducer(first, second):

    return (first[0] + second[0], first[1] + second[1], first[2], first[3], first[4])    



kafkaStream.transform(storeOffsetRanges).foreachRDD(printOffsetRanges)



print("Waiting here : ")

lines = kafkaStream.map(lambda x: x[1])

# lines.pprint()

# fm = lines.flatMap(split)

# count = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a,b: a + b)

# count = lines.flatMap(split).map(lambda word: (word.split(" : ")[0], int(word.split(" : ")[1]))).reduceByKey(lambda a,b: a + b)

count = lines.flatMap(split).map(mapper).reduceByKey(reducer)

# res = count.map(lambda elem : list(elem))

# print(res)

count.foreachRDD(publish)

count.pprint()

ssc.start()

ssc.awaitTermination()



# text_file = sc.textFile("./HelloWorld.java")



# counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a,b: a + b)



# counts.saveAsTextFile("./counts")



print("Success is not unachievable")


