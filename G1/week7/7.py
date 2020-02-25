import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["test"]
mycol = mydb["restaurants"]

myquery = {"name": "Morris Park Bake Shop"}

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)