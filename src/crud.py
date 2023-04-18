from sqlalchemy.orm import Session

import models


def get_product_by_id(db: Session, nm_id: int):
    product = db.query(models.Product).filter(
        models.Product.nm_id == nm_id).first()
    return product


def get_all_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()
