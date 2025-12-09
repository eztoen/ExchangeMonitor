from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.core.models.Redis.redis_helper import redis_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = await redis_helper.get_client()
    
    yield
    
    await redis_helper.close()
        
app = FastAPI(lifespan=lifespan)