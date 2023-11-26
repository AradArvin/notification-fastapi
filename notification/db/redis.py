from redis import asyncio as aioredis

from core import settings


HOST_ADDRESS: str = settings.REDIS_HOST_ADDRESS 

redis = aioredis.from_url(HOST_ADDRESS, decode_responses=True)


# Redis check otp key 

async def save_otp_to_redis(user_id: str, otp: str):
    
    key = f"user_{user_id}"

    await redis.set(name=key, value=otp, ex=180)
