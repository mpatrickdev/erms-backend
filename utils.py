import cloudinary
import cloudinary.uploader

from typing import Tuple
from fastapi import UploadFile

from config import settings

cloudinary.config( 
  cloud_name = settings.cloudinary_name, 
  api_key = settings.cloudinary_api_key, 
  api_secret = settings.cloudinary_api_secret
)

def cloudinary_upload(file: UploadFile) -> Tuple:
  # upload to cloudinary
  result = cloudinary.uploader.upload(file.file)
  # print(result)
  url = result['url']
  cloudinary_id = result['public_id']
  return url, cloudinary_id

def cloudinary_destroy(cloudinary_id: str):
  cloudinary.uploader.destroy(cloudinary_id)
  return