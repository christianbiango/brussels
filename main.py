from fastapi import FastAPI
from app.database.connect import DatabaseConnect
from app.routers import insert_data


app = FastAPI(title="Brussels - Data", description="Les données de Brussels", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    print('App started')
    await DatabaseConnect.conn()

app.include_router(insert_data.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

