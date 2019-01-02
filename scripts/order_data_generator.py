#!flask/bin/python
from flask import Flask
from flask import request
from pymongo import MongoClient
import random
import sys
import json
import numpy 

states = ['Alabama','Alaska','American Samoa','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Federated States of Micronesia','Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Palau','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

app = Flask(__name__)
@app.route('/postjson', methods=['POST'])

def post():

	client = MongoClient()


	client = MongoClient('localhost', 27017)
	db = client.test
	users = db.users
	products=db.products
	dic={}
	count = int(request.args.get("count"))
	for val in range(0,count):
		ra=generateBaisedRandom()
		user_data=users.find_one({"name": "user"+str(ra)})
		ra=generateBaisedRandom()
		product_data=products.find_one({"pname": "product"+str(ra)})


		merged_dict = {key: value for (key, value) in (user_data.items() + product_data.items())}

		#jsonString_merged = json.dumps(merged_dict)
		del(merged_dict['_id'])
		merged_dict['rating'] = random.uniform(1, 5)
		x = helper(12)

		y = helper(50)


		merged_dict['purchase_month'] = months[x]
		merged_dict['state'] = states[y] 
		dic[str(val)]=merged_dict
		#print("")

#	print(dic)
	return json.dumps(dic,sort_keys=False, indent = 4, separators = (',',':'))
	

def generateBaisedRandom():
	data=[2,10,50,60,160,180,181,208,234,324,580,765]
	ra=random.randint(1,208)
	i=0
	while i<9:
		i=i+1
		if data[i]>ra:
			return i


def helper(end):
	x = numpy.random.normal(0, 0.1) * end/2 + end/2
	if x < 0:
		return 0
	for i in range(0, end):
		if x >= i and x < i+1:
			return i

	return end



app.run(host='0.0.0.0', port=5000)


