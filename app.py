from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routes import blog_router

app = FastAPI()

# MongoDB connection
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client.school_blog

app.include_router(blog_router)
