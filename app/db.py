from motor.motor_asyncio import AsyncIOMotorClient
import os

client = None
db = None

def get_mongo_uri():
    return os.getenv("MONGO_URI")

async def connect_db():
    global client, db
    uri = get_mongo_uri()
    client = AsyncIOMotorClient(uri)
    db = client.get_default_database()
    # create indexes here if needed

async def close_db():
    global client
    if client:
        client.close()
