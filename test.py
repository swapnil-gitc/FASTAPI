from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017")
docs = conn.notes.notes.find_one({})
print(docs)