import motor.motor_asyncio as motor
import sys
from app.config.env import MONGO_ENV, COLLECTION_ENV
from motor.motor_asyncio import AsyncIOMotorClient

class DatabaseConnect:
    @classmethod
    def __init_credentials(cls):
        cls.__mongo_uri = MONGO_ENV['MONGO_URI']
        cls.__client = AsyncIOMotorClient(cls.__mongo_uri)
        cls._brussels_db_name = MONGO_ENV['DB_NAME']
        

    @classmethod
    async def conn(cls):
        cls.__init_credentials()
        await cls.__client_conn()
        await cls.__client_ping()
            
        await cls.__brussels_db_exists()
        await cls.__create_brussels_collections_dict()

        collections = [
            COLLECTION_ENV['DATA_COLLECTION'],
        ]
        for collection in collections:
            try:
                await cls.__create_collection_if_nonexistent(collection)
            except Exception as e:
                print(e, f"Message : Erreur non attrapée lors de la création de la collection `{collection[0]}`")
                sys.exit()
    
    @classmethod
    async def __create_collection_if_nonexistent(cls, collection_name_env):
        if collection_name_env in cls._brussels_db_collections_list:
            return None
        else:
            try:
                await cls._brussels_db.create_collection(collection_name_env)
            except Exception as e:
                print(f"Message : Erreur avec Motor lors de la création de la collection `{collection_name_env}`")
                sys.exit()
            else:
                print(f"La collection `{collection_name_env}` a été créée avec succès.")

            # Ajouter la collection au dict des collections et à la liste des collections
            cls._all_brussels_collections_dict[collection_name_env] = cls._brussels_db[collection_name_env]
            cls._brussels_db_collections_list.append(collection_name_env)

    @classmethod
    async def __brussels_db_exists(cls):
        try:
            db_list = await cls._mongo_client.list_database_names()
        except Exception as e:
            print(f"Message : Erreur pour récupérer la liste des bases de données du Client Mongo")
            sys.exit()

        cls.__select_brussels_db()

        if cls._brussels_db.name not in db_list:
            print(f"Not Found: La DB `{cls._brussels_db.name}` n'existe pas")
            sys.exit()
    
    @classmethod
    async def __client_conn(cls):
        try:
            cls._mongo_client = motor.AsyncIOMotorClient(cls.__mongo_uri)
            
        except Exception as e:
            print("Message : Erreur lors de la création d'un Client Mongo")
            sys.exit()
    
    @classmethod
    async def __client_ping(cls):
        try:
            cls._mongo_client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(f"Message : Erreur lors du ping du Client Mongo")
            sys.exit()
    
    @classmethod
    def __select_brussels_db(cls):
        cls._brussels_db = cls._mongo_client[cls._brussels_db_name]
    
    @classmethod
    async def __create_brussels_collections_dict(cls):
        try:
            cls._brussels_db_collections_list = await cls._brussels_db.list_collection_names()
        except Exception as e:
            print(f"Message : Erreur inconnue lors de la récupération des collections de la bdd `{cls._brussels_db.name}`")
            sys.exit()
        collections_dict = {}

        for col in cls._brussels_db_collections_list:
            collections_dict[col] = cls._brussels_db[col]

        cls._all_brussels_collections_dict = collections_dict

    @classmethod
    def get_brussels_collection(cls, collection_name_env):
        return cls._all_brussels_collections_dict[collection_name_env]