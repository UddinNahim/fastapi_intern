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
    name: str | None = None
    description: str | None = None
    instructor: str | None = None
    rating: float | None = None
    price: int | None = None

class CourseView(BaseModel):
    name: Optional[str]

class CourseJoinView(BaseModel):
    name: Optional[str]
    instructor: Optional[str]