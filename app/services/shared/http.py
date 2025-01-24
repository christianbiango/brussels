import httpx

class HTTPService:
    @staticmethod
    async def get(endpoint, params = None, headers = None):
        async with httpx.AsyncClient() as client:
            return await client.get(endpoint, params=params, headers=headers)
        
    @staticmethod
    async def post(endpoint, data, headers = None):
        async with httpx.AsyncClient() as client:
            res = await client.post(endpoint, json=data, headers=headers)
        return res.json()