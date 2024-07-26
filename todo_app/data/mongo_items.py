import pymongo
import os

client = pymongo.MongoClient(os.getenv("MONGO_CONNECTION_STRING"))

db =client[os.getenv("MONGO_DATABASE_NAME")]

collection = db[os.getenv("MONGO_COLLECTION_NAME")]


def add_item(new_todo_title: str):
    new_item = {
        "name": new_todo_title,
        "status": "To Do"
    }


    collection.insert_one(new_item)

def get_items():
    pass

def move_item_to_done():
    pass