from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from sqlalchemy import LargeBinary  # Import LargeBinary

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    body_html: str
    vendor: Optional[str] = None
    status: Optional[str]
    price: float
    stock: int
    image: Optional[bytes]  # Use LargeBinary for image
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
