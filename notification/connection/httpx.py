import httpx

from core import settings

# HTTP_X request to account app data endpoint.

async def httpx_response(data_endpoint:str, data: dict):
    
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{settings.DATA_ADDRESS}/{data_endpoint}", json=data)

    return response.json()


