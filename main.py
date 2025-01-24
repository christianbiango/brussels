from fastapi import FastAPI
from app.database.connect import DatabaseConnect


app = FastAPI(title="Brussels - Data", description="Les données de Brussels", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    print('App started')
    await DatabaseConnect.conn()

@app.get("/items")
async def get_items():
    items = await db["items"].find().to_list(length=None)
    for item in items:
        item["_id"] = str(item["_id"])
    return {"items": items}


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

