from pydantic import BaseModel
from typing import List


# ====================================
# PRICE HISTORY SCHEMAS
# ====================================
class PriceHistoryBase(BaseModel):
    day: str
    your_price: float
    amazon_price: float
    flipkart_price: float


class PriceHistoryResponse(PriceHistoryBase):
    id: int
    product_id: int

    class Config:
        from_attributes = True


# ====================================
# PRODUCT SCHEMAS
# ====================================
class ProductBase(BaseModel):
    product_name: str
    your_price: float
    amazon_price: float
    flipkart_price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    history: List[PriceHistoryResponse] = []

    class Config:
        from_attributes = True


# ====================================
# USER AUTH SCHEMAS
# ====================================
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


# ====================================
# JWT TOKEN SCHEMAS
# ====================================
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None