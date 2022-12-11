from fastapi import APIRouter

from .endpoints import product

router = APIRouter(prefix='/api')

router.include_router(product.router)