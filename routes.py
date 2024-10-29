from fastapi import APIRouter, HTTPException
from models import BlogPost
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

router = APIRouter()

@router.post("/posts/", response_model=BlogPost)
async def create_post(post: BlogPost):
    post_dict = post.dict()
    result = await db.posts.insert_one(post_dict)
    post_dict['_id'] = str(result.inserted_id)
    return post_dict

@router.get("/posts/{post_id}", response_model=BlogPost)
async def read_post(post_id: str):
    post = await db.posts.find_one({"_id": ObjectId(post_id)})
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
