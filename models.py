from datetime import datetime
from typing import List, Optional, Tuple

from beanie import Document, Link
from pydantic import BaseModel

#------SHARED 
class Image(BaseModel):
  url: str
  cloudinary_id: Optional[str]

class GeoObject(BaseModel):
  type: str = 'Point'
  coordinates: Tuple[float, float]

#Line item
class LineItem(BaseModel):
  sku: str
  name: str
  quantity: int
  price: int
#-------------

class Customer(Document):
  name: str
  phone: str
  location: Optional[GeoObject]
  created_at: datetime = datetime.now()


class Staff(Document):
  name: str
  phone: str
  department: Optional[str]
  created_at: datetime = datetime.now()

class User(Document):
  username: str
  password: str
  created_at: datetime = datetime.now()

class Store(Document):
  name: str
  phone: str
  # location: Optional[Tuple[float, float]]
  created_at: datetime = datetime.now()

class StoreRef(BaseModel):
  name: str

class Product(Document):
    sku: str
    name: str
    description: Optional[str]
    category: Optional[str]
    image: Optional[Image]
    price: int
    # currency: Optional[str] = 'UGX'
    created_at: datetime = datetime.now()

class ProductCreate(BaseModel):
    sku: str
    name: str
    description: str
    category: Optional[str]
    price: int

class ProductUpdate(BaseModel):
    sku: Optional[str]
    name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    price: Optional[int]

class ProductRef(BaseModel):
  sku: str
  name: str

class Order(Document):
  items: List[LineItem] = []
  total: int

class Inventory(Document):
  store_id: str
  product: ProductRef
  quantity: int
  created_at: datetime = datetime.now()

