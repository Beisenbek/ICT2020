import pymongo


#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
print(myclient.list_database_names())
