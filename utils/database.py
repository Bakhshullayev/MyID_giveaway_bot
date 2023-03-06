from motor import motor_asyncio

from config import settings


class MongoDB:
    def __init__(self):
        if settings.debug:
            self.client = motor_asyncio.AsyncIOMotorClient(host="localhost", port=27017)
        else:
            self.client = motor_asyncio.AsyncIOMotorClient(
                host=settings.db_host,
                port=settings.db_port,
                username=settings.db_username,
                password=settings.db_password,
            )
        self.db = self.client[settings.db_database]

    async def language(self, user_id: int, language: str = None):
        """Get user language"""
        if language:
            await self.db.language.update_one(
                filter={"user_id": user_id},
                update={"$set": {"lang": language}},
                upsert=True,
            )

        if await self.db.language.find_one({"user_id": user_id}) is None:
            await self.db.language.insert_one({"user_id": user_id, "lang": "uz"})

        data = await self.db.language.find_one({"user_id": user_id})
        return data.get('lang')

    async def user_info(self, user_id):
        if await self.db.users.find_one({"user_id": user_id}) is None:
            self.db.users.insert_one({"user_id": user_id})

        return await self.db.users.find_one({"user_id": user_id})

    async def update_info(self, user_id: str, data: dict) -> None:
        self.db.users.update_one({"user_id": user_id}, {"$set": data}, upsert=True)


db = MongoDB()
