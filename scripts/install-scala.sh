#!/bin/bash

sudo apt-get update -y

sudo apt-get install scala -y

wget http://mirror.olnevhost.net/pub/apache/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz

tar xvf spark-2.4.0-bin-hadoop2.7.tgz

sudo mv spark-2.4.0-bin-hadoop2.7 /usr/local/spark

sudo echo "export PATH=\$PATH:/usr/local/spark/bin" >> ~/.bashrc

source ~/.bashrc

spark-shell
