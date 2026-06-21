from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# ====================================
# PRODUCT MODEL
# ====================================
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    your_price = Column(Float, nullable=False)
    amazon_price = Column(Float, nullable=False)
    flipkart_price = Column(Float, nullable=False)

    history = relationship(
        "PriceHistory",
        back_populates="product",
        cascade="all, delete-orphan"
    )


# ====================================
# PRICE HISTORY MODEL
# ====================================
class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    day = Column(String, nullable=False)
    your_price = Column(Float, nullable=False)
    amazon_price = Column(Float, nullable=False)
    flipkart_price = Column(Float, nullable=False)

    product = relationship(
        "Product",
        back_populates="history"
    )


# ====================================
# USER MODEL (JWT AUTH)
# ====================================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String,
        nullable=False
    )