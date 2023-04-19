from datetime import datetime
from typing import Dict

from product_parser import wb_parser

from sqlalchemy.orm import Session

import models
import schemas


def get_product_by_id(db: Session, nm_id: int):
    product = db.query(models.Product).filter(
        models.Product.nm_id == nm_id).first()
    return product


def get_all_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product_data: {schemas.ProductBase}):
    db_product = models.Product(**product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(nm_id: int, db: Session):
    product_data = wb_parser(nm_id)
    if product_data:
        try:
            product = db.query(models.Product).filter(
                models.Product.nm_id == nm_id).first()
            if product:
                product_data.update({"updated_at": datetime.now()})
                product_update = schemas.ProductBase(**product_data)
                db.query(models.Product).filter(
                    models.Product.nm_id == nm_id).update(
                    product_update.dict())
                db.commit()
        finally:
            db.close()
