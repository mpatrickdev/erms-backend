from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import Product, User


async def init_db():
    client = AsyncIOMotorClient(settings.database_url)
    await init_beanie(
        database=client[settings.database_name],
        document_models=[Product, User],
    )