from typing import List, Optional
from fastapi import HTTPException
from passlib.context import CryptContext


from .base import ServiceBase
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)

class UserService(ServiceBase):
  model = User

  async def create(self, obj: dict):
    # Check username & email
    username = await self.find({'username': obj['username']})
    if username is not None:
      raise HTTPException(
        status_code=400,
        detail='Username taken'
      )
    email = await self.find({'email': obj['email']})
    if email is not None:
      raise HTTPException(
        status_code=400,
        detail='Email taken'
      )

    # hash password
    obj['password'] = get_password_hash(obj['password'])

    # save
    db_obj = self.model(**obj)
    return await db_obj.create() 

  async def verify(self, obj: dict):
    db_obj = await self.find({'username': obj['username']})
    
    if not db_obj:
      return False

    if not verify_password(obj['password'], db_obj.password):
      return False

    return db_obj


user_service = UserService()