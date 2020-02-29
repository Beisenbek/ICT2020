import pymongo


myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }

x = mycol.find_one()

print(x)