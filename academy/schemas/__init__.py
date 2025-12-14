from pydantic import BaseModel, Field 
from datetime import datetime
from typing import Optional

class CourseCreate(BaseModel):
    name: str
    description: str
    instructor: str
    rating: float = Field(default=0.0, ge=0,le=5)
    price: int

class CourseResponse(BaseModel):
    id: int
    name: str
    description: str
    instructor: str
    rating : float
    price: int
    created_on: datetime

class CourseUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    instructor: Optional[str]
    rating: Optional[float]
    price: Optional[int]