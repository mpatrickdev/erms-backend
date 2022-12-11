from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from models import Product, ProductCreate, ProductUpdate
from api.services.product import product_service

router = APIRouter(prefix='/products', tags=['Product'])

async def find_or_404(id: str):
  db_obj = await product_service.get(id)
  if db_obj is None:
      raise HTTPException(status_code=404, detail="Product not found")
  return db_obj


@router.get('')
async def list_products(category: str = None):
  if category is not None:
    return await product_service.find({'category': category})
  return await product_service.all()

@router.get('/{id}')
async def read_product(db_obj: Product = Depends(find_or_404)):
  return db_obj

@router.post('/')
async def create_product(obj: ProductCreate):
  return await product_service.create(obj.dict())  

@router.put('/{id}')
async def update_product(obj: ProductUpdate, id: str, db_obj: Product = Depends(find_or_404)):
  return await product_service.update(id, obj.dict())

@router.delete('/{id}')
async def destroy_product(id: str, db_obj: Product = Depends(find_or_404)):
  return await product_service.delete(id)

@router.post('/{id}/upload-image')
async def create_product(id: str, file: UploadFile = File(...)):
  return await product_service.upload_image(id, file) 
