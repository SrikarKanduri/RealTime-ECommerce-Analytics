# RealTime_ECommerce_Analytics

![alt text](https://raw.github.ncsu.edu/skanama/RealTime_ECommerce_Analytics/master/img/architecture.png?token=AAAioGtSpH0qpW5Ndr0SZ70OJSV6FdACks5cG_4ewA%3D%3D)

# 1. Stream Data
1) Install Mongo 
```
$ cd scripts
$ chmod +x mongo-install.sh
$ ./mongo-install.sh
```
2) Run Mongo server
```
$ sudo serivce mongod start 
```
3) Populate users DB
```
$ mongo localhost:27017/test user_data_generator.js
```
4) Populate products DB
```
$ mongo localhost:27017/test product_data_generator.js
```
5) Generate and stream orders data
```
$ python order_data_generator.py
```

# 2. Run Kafka Brokers
1) Install and run Kafka 
```
$ cd scripts
$ chmod +x install-kafka.sh
$ ./install-kafka.sh
```
2) Run Kafka Producer
```
$ cd src
$ javac -cp "<KAFKA_HOME>/libs/*":gson-2.8.2.jar SimpleProducer.java 
$ java -cp "<KAFKA_HOME>/libs/*":gson-2.8.2.jar:. SimpleProducer <topic> <#-records> 
```

# 3. Run Spark Nodes
1) Install and run Spark 
```
$ cd scripts
$ chmod +x install-spark.sh
$ ./install-spark.sh (This script deploys the spark application as well)
```
2) Run Kafka consumer (This is required to push the aggregated data to MongoDB)
```
$ cd src
$ python KafkaConsumer.py
```

# 4. Visualize trends
Go to http://152.46.19.85/dashboards and login
