import pymongo


def getConnection():
    mongo = pymongo.MongoClient(host="localhost", port=27017)
    mongo.server_info()
    return mongo