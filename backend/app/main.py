from fastapi import FastAPI
from app.routes.builder import router as builder_router

app = FastAPI()

app.include_router(builder_router, prefix="/api/builder")