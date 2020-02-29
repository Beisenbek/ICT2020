import pymongo


myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$lt": "I" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)