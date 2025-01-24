from app.database.shared.methods import SharedDatabaseMethods

class SharedOperationsService:    
    async def fetch(self, collection_name_env, query: dict):
        return await SharedDatabaseMethods.fetch_database_collection(collection_name_env, query)
    
    async def sorted_fetch(self, collection_name_env, query: dict, **sort):
        return await SharedDatabaseMethods.fetch_database_collection_sorted(collection_name_env, query, field=sort['field'], by=sort['by'])
    
    async def fetch_by_id(self, collection_name_env, query:dict):
        return await SharedDatabaseMethods.find_one_in_collection(collection_name_env, query)
    
    async def insert_one_in_collection(self, collection_name_env, query:dict):
        return await SharedDatabaseMethods.insert_one_in_collection(collection_name_env, query)
    
    async def insert_many_in_collection(self, collection_name_env, query:dict):
        print(query)
        return await SharedDatabaseMethods.insert_many_in_collection(collection_name_env, query)