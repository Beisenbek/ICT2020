import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["test"]
mycol = mydb["restaurants"]

for x in mycol.find():
  print(x)