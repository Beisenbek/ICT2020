import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["test"]
mycol = mydb["restaurants"]


myquery = { "name": "May May Kitchen" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)


