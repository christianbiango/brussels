from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from app.config.env import MONGO_ENV
from motor.motor_asyncio import AsyncIOMotorClient

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('App started')
    yield
    print('App is shutting down')

app = FastAPI(title="Brussels - Data", description="Les données de Brussels", version="1.0.0")

# Configuration MongoDB
MONGO_URI = MONGO_ENV['MONGO_URI']
DB_NAME = MONGO_ENV['DB_NAME']
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

@app.get("/items")
async def get_items():
    items = await db["items"].find().to_list(length=None)
    for item in items:
        item["_id"] = str(item["_id"])
    return {"items": items}


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

