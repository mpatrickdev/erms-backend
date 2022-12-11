from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from database import init_db
from api import api_router

app = FastAPI()



app = FastAPI()

origins = [
  'http://localhost:9000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def start_db():
    await init_db()


@app.get('/health')
async def health():
    return {"status": "ok"}

app.include_router(api_router.router)