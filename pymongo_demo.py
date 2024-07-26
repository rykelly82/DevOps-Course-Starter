import pymongo
import dotenv
import os

dotenv.load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_CONNECTION_STRING"))

db =client.todoappdatabase

collection = db.todo_items

# Insert a record
collection.insert_one({"description": "A pymongo document"})

# Read all records

list(collection.find())


# Insert and update a record
collection.insert_one({"description": "An updateable document document", "type": "updateable"})
collection.update_one({"type": "updateable"}, {"$set": {"description": "CHANGED!!!"}})




print(collection)