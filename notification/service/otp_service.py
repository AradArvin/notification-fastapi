from random import randint

from db.redis import save_otp_to_redis


class OTPService:

    def __init__(self) -> None:
        pass

    async def otp_action(self, user_id: str) -> str:

        otp = str(randint(1000, 9999))
        await save_otp_to_redis(user_id, otp)

        return otp

