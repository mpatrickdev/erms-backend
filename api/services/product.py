from fastapi import UploadFile

from utils import cloudinary_destroy, cloudinary_upload
from .base import ServiceBase
from models import Product, Image

class ProductService(ServiceBase):
  model = Product

  async def upload_image(self, id: str, file: UploadFile):
    url, cloudinary_id = cloudinary_upload(file)
    # Save image
    image = Image(url=url, cloudinary_id=cloudinary_id)
    
    db_obj = await self.get(id)
    if db_obj.image:
      # remove old image
      cloudinary_destroy(db_obj.image.cloudinary_id)

    db_obj.image = image
    return await db_obj.save()


  
product_service = ProductService()