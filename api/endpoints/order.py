from fastapi import APIRouter, Depends, HTTPException

from app.models.order import Order, OrderCreate, OrderUpdate, OutputItem
from app.services.order import order_service

router = APIRouter(prefix='/orders', tags=['Order'])

async def find_or_404(id: str):
  db_obj = await order_service.get(id)
  if db_obj is None:
      raise HTTPException(status_code=404, detail="Order not found")
  return db_obj


@router.get('')
async def list_orders(customer: str = None):
  if customer is not None:
    return await order_service.find_by({'customer': customer})
  return await order_service.all()

@router.get('/stats')
async def list_orders():
  pipline = {}
  result = await Order.aggregate(
    [{"$group": {"_id": "$items.name", "total": {"$avg": "$price"}}}],
    projection_model=OutputItem
).to_list()
  return result

@router.get('/{id}')
async def read_order(db_obj: Order = Depends(find_or_404)):
  return db_obj

@router.post('/')
async def create_order(obj: OrderCreate):
  return await order_service.create(obj.dict())  

@router.put('/{id}')
async def update_order(obj: OrderUpdate, id: str, db_obj: Order = Depends(find_or_404)):
  return await order_service.update(id, obj.dict())

@router.delete('/{id}')
async def destroy_order(id: str, db_obj: Order = Depends(find_or_404)):
  return await order_service.delete(id)
