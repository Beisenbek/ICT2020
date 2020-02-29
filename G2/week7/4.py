import pymongo


myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }

for x in mycol.find():
  print(x)

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)