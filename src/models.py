from sqlalchemy import Column, Integer, String

from database import Base


class Product(Base):
    __tablename__ = "products"

    nm_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    brand = Column(String)
    brand_id = Column(Integer)
    site_brand_id = Column(Integer)
    supplier_id = Column(Integer)
    sale = Column(Integer)
    price = Column(Integer)
    sale_price = Column(Integer)
    rating = Column(Integer)
    feedbacks = Column(Integer)
    colors = Column(String)
