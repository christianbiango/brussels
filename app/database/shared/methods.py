from app.database.connect import DatabaseConnect
class SharedDatabaseMethods(DatabaseConnect):
    # READ
    @classmethod
    async def fetch_database_collection(cls, collection_name_env, query, exclude_terms = {}):
        collection_data = cls.get_brussels_collection(collection_name_env).find(query, exclude_terms)
        return await collection_data.to_list(length=None)
    
    @classmethod
    async def fetch_database_collection_sorted(cls, collection_name_env, query, exclude_terms = {}, **sort):
        collection_data = cls.get_brussels_collection(collection_name_env).find(query, exclude_terms).sort(sort['field'], sort['by'])
        return await collection_data.to_list(length=None)

    @classmethod
    async def find_one_in_collection(cls, collection_name_env, query:dict, exclude_terms = {}):
        return await cls.get_brussels_collection(collection_name_env).find_one(query, exclude_terms)

    # CREATE
    @classmethod
    async def insert_many_in_collection(cls, collection_name, list_of_dicts):
        return await cls.get_brussels_collection(collection_name).insert_many(list_of_dicts, ordered=True)
    
    @classmethod
    async def insert_one_in_collection(cls, collection_name_env, data):
        print(data)
        return await cls.get_brussels_collection(collection_name_env).insert_one(data)

    # UPDATE

    @classmethod
    async def update_many_in_collection(cls, collection_name_env, filter_criteria, update_query):
        return cls.get_brussels_collection(collection_name_env).many(filter_criteria, update_query)
    
    @classmethod
    async def update_one_in_collection(cls, collection_name_env, filter_criteria, update_query):
        return await cls.get_brussels_collection(collection_name_env).update_one(filter_criteria, update_query)
    
    # DELETE
    @classmethod
    async def delete_many_in_collection(cls, collection_name_env, filters):        
        return await cls.get_brussels_collection(collection_name_env).delete_many({"$or": filters})
    
    @classmethod
    async def delete_one_in_collection(cls, collection_name_env, target_query:dict):        
        return await cls.get_brussels_collection(collection_name_env).delete_one(target_query)