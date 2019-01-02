sudo apt-get install scala -y
sudo apt-get install python-pip -y
pip install kafka-python
pip install pymongo
wget https://www-eu.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
tar xvf spark-2.4.0-bin-hadoop2.7.tgz
sudo apt-get install openssh-server openssh-client -y
ssh-keygen -t rsa -P ""
spark-2.4.0-bin-hadoop2.7/bin/spark-submit --jars Downloads/spark-streaming-kafka-0-8-assembly_2.11-2.4.0.jar --master local Downloads/sparktest.py