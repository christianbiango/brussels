from dotenv import load_dotenv
import os

load_dotenv()

MONGO_ENV = {
    "MONGO_URI": os.getenv("MONGO_URI"),
    "DB_NAME": os.getenv("DB_NAME"),
}

COLLECTION_ENV = {
    "DATA_COLLECTION": os.getenv("DATA_COLLECTION"),
}

ENDPOINT_ENV = {
    "BASE_URL": os.getenv("BASE_URL"),
}