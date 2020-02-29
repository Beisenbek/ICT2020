import pymongo


myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict1 = { "name": "John", "address": "Highway 37" }
mydict2 = { "name": "John", "address": "Highway AB" }
mydict3 = { "name": "John", "address": "Highway 37B" }
mydict4 = { "name": "John", "address": "Highway 37C" }

x = mycol.insert_one(mydict1)
print(x.inserted_id)

x = mycol.insert_one(mydict2)
print(x.inserted_id)

x = mycol.insert_one(mydict3)
print(x.inserted_id)

x = mycol.insert_one(mydict4)
print(x.inserted_id)
