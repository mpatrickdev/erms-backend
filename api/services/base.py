from beanie import Document, PydanticObjectId

class ServiceBase:
  model: Document

  async def all(self):
    return await self.model.find_all().to_list()

  async def find_one(self, filter: dict):
    return await self.model.find_one(filter)

  async def find(self, filter: dict):
    return await self.model.find(filter).to_list()

  # async def find_near(self, filter: dict):
  #   return await self.model.find(filter).to_list()

  async def get(self, id: str):
    return await self.model.get(id)

  async def create(self, obj: dict):
    db_obj = self.model(**obj)
    return await db_obj.create()

  async def update(self, id: str, obj: dict):
    db_obj = await self.get(id)
    data = {k: v for k, v in obj.items() if v is not None}
    await db_obj.update({"$set": data})
    return db_obj

  async def delete(self, id: str):
    db_obj = await self.get(id)
    return await db_obj.delete()