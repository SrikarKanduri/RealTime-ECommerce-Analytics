#!/bin/bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get update -y
sudo apt-get install oracle-java8-installer -y
sudo java -version
sudo apt-get install zookeeperd -y
netstat -ant | grep :2181
wget https://www-eu.apache.org/dist/kafka/2.1.0/kafka_2.12-2.1.0.tgz
sudo mkdir /opt/Kafka
sudo tar -xvf kafka_* -C /opt/Kafka
sudo  /opt/Kafka/kafka_*/bin/kafka-server-start.sh /opt/Kafka/kafka_*/config/server.properties
