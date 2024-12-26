from fastapi import FastAPI
from contextlib import asynccontextmanager

def create_app():
    app = FastAPI(lifespan=lifespan)
    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    await register_routers(app)
    yield
    await app.router.shutdown()

async def register_routers(app: FastAPI):
    from app.api.test1 import router as test1_router
    from app.api.test3 import router as test3_router
    from app.api.test import router as test_router
    
    app.include_router(test1_router)
    app.include_router(test3_router)
    app.include_router(test_router)
