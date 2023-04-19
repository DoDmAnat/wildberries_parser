from datetime import datetime
from product_parser import wb_parser
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import insert

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="wildberries parser"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/products/{nm_id}/")
def create_product(nm_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.nm_id == nm_id).first()
    if product:
        print(db.query(models.Product.nm_id))
        return 'Товар уже существует в базе данных'
    product_data = wb_parser(nm_id)
    if product_data:
        return crud.create_product(db=db, product_data=product_data)
    return 'Нет такого товара'


@app.get("/products/{nm_id}/", response_model=schemas.ProductBase)
def read_product(nm_id: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, nm_id=nm_id)
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return product


@app.get("/products/", response_model=List[schemas.ProductBase])
def read_products(skip: int = 0, limit: int = 100,
                  db: Session = Depends(get_db)):
    products = crud.get_all_products(db, skip=skip, limit=limit)
    return products


@app.delete("/products/{nm_id}/")
def delete_product(nm_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.nm_id == nm_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    db.delete(product)
    db.commit()
    return f"Товар '{nm_id}' удален"


# @app.patch("/products/update/{nm_id}/")
# def update_product(nm_id: int, db: Session = Depends(get_db)):
#     crud.update_product(db=db, nm_id=nm_id)
#     return {'status': 'OK'}