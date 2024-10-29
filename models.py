from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class BlogPost(BaseModel):
    title: str = Field(..., max_length=100)
    content: str = Field(..., min_length=10)
    author: str = Field(..., max_length=50)

    class Config:
        json_encoders = {
            ObjectId: str
        }
