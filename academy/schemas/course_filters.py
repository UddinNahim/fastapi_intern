from pydantic import BaseModel, field_validator
from datetime import datetime
from decimal import Decimal
from typing import Optional, Literal


class CourseFilter(BaseModel):
    # -------- filters --------
    min_price: Optional[Decimal] = None
    max_price: Optional[Decimal] = None

    min_rating: Optional[float] = None
    max_rating: Optional[float] = None

    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    # -------- sorting --------
    sort_by: Literal["name", "price", "rating","instructor"] = "price"
    order: Literal["asc", "desc"] = "asc"

    # -------- validators --------

    @field_validator("max_price")
    @classmethod
    def validate_price_range(cls, max_price, info):
        min_price = info.data.get("min_price")
        if min_price is not None and max_price is not None:
            if min_price > max_price:
                raise ValueError("min_price cannot be greater than max_price")
        return max_price

    @field_validator("max_rating")
    @classmethod
    def validate_rating_range(cls, max_rating, info):
        min_rating = info.data.get("min_rating")
        if min_rating is not None and max_rating is not None:
            if min_rating > max_rating:
                raise ValueError("min_rating cannot be greater than max_rating")
        return max_rating

    @field_validator("min_rating", "max_rating")
    @classmethod
    def validate_rating_bounds(cls, rating):
        if rating is not None and not (0 <= rating <= 5):
            raise ValueError("rating must be between 0 and 5")
        return rating

    @field_validator("end_date")
    @classmethod
    def validate_date_range(cls, end_date, info):
        start_date = info.data.get("start_date")
        if start_date and end_date and start_date > end_date:
            raise ValueError("start_date cannot be after end_date")
        return end_date
