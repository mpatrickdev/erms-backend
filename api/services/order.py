from typing import List, Optional
from fastapi import HTTPException


from .base import ServiceBase
from models import Order

class OrderService(ServiceBase):
  model = Order

order_service = OrderService()