from fastapi import APIRouter, Depends, HTTPException

from models import GeoObject
from models import Customer, CustomerCreate, CustomerUpdate
from api.services.customer import customer_service

router = APIRouter(prefix='/customers', tags=['Customer'])

async def find_or_404(id: str):
  db_obj = await customer_service.get(id)
  if db_obj is None:
      raise HTTPException(status_code=404, detail="Product not found")
  return db_obj


@router.get('')
async def list_customers():
  return await customer_service.all()

@router.get('/search')
async def geo_locate_customers(long: float, lat: float):
  point = GeoObject(coordinates=[long, lat])
  places = await Customer.aggregate([
    {
      "$geoNear": {
        "near": point.dict(),
        "distanceField": "distance",
        "maxDistance": 1000 # 1km
      }
    }
  ],
    projection_model=Customer).to_list()

  # places =await Customer.find({
  #   "geo":
  #   {
  #     "$near": {
  #       "$geometry": {
  #         "type": "Point",
  #         "coordinates": [long, lat],
  #         "$maxDistance": 5000
  #       }
  #     }
  #   }
  # }).to_list()

  return places

@router.get('/{id}')
async def read_customer(db_obj: Customer = Depends(find_or_404)):
  return db_obj

@router.post('/')
async def create_customer(obj: CustomerCreate):
  return await customer_service.create(obj.dict())  

@router.put('/{id}')
async def update_customer(obj: CustomerUpdate, id: str, db_obj: Customer = Depends(find_or_404)):
  return await customer_service.update(id, obj.dict())

@router.delete('/{id}')
async def destroy_customer(id: str, db_obj: Customer = Depends(find_or_404)):
  await customer_service.delete(id)
  return
