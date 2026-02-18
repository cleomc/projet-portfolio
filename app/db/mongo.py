from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client: AsyncIOMotorClient = None
db = None


async def connect_mongo():
    """Ouvre la connexion MongoDB."""
    global client, db
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.MONGO_DB_NAME]
    print(f"✅ MongoDB connecté — base : {settings.MONGO_DB_NAME}")


async def close_mongo():
    """Ferme la connexion MongoDB."""
    global client
    if client:
        client.close()
        print("🔌 MongoDB déconnecté")


def get_db():
    """Retourne la base MongoDB courante."""
    return db
