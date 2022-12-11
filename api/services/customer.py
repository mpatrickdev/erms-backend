from .base import ServiceBase
from models import Customer

class CustomerService(ServiceBase):
  model = Customer

  
customer_service = CustomerService()