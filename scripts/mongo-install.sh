#!/bin/bash
# Import the public key used by the package management system
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

#echo '*************** Public Key Imported Successfully ***********'

# Create a list file for MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

#echo '***************  List file created successfully  ***********'

# Reload local package database
sudo apt-get update

# Install the latest stable version of MongoDB
sudo apt-get install -y mongodb-org

#echo '***************  Mongodb installed successfully  ***********'

# Edit bindIp in /etc/mongod.conf to allow any remote client to connect to mongodb
sudo sed -i 's/bindIp:.*/bindIp: 0.0.0.0/g' /etc/mongod.conf # TODO : take care of security. donot allow unauthorized users and ips to connect

#echo '***************  Edited mongod.conf successfully  ***********'

# Edit the firewall settings and allow access from any ip to the port on which mongodb is running. DEFAULT : 27017
var=`grep -n REJECT /etc/iptables.rules | cut -d":" -f1`
sed -i "${var}i -A INPUT -p tcp --dport 27017 -j ACCEPT" /etc/iptables.rules
sudo iptables-restore < /etc/iptables.rules

#echo '***************   updated iptables successfully   ***********'

# Start mongodb service
sudo service mongod start

echo '***************  Mongdb started  ***********'

mongo localhost:27017/video-db populate-video-db.js
