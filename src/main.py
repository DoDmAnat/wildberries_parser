from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.sql import insert
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from parser import wb_parser
import models
import schemas
import crud

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
    data = wb_parser(nm_id)
    if data:
        conn = engine.connect()
        ins = insert(models.Product).values(
            nm_id=nm_id,
            name=data['name'],
            brand=data['brand'],
            brand_id=data['brandId'],
            site_brand_id=data['siteBrandId'],
            supplier_id=data['supplierId'],
            sale=data['sale'],
            price=data['priceU'],
            sale_price=data['salePriceU'],
            rating=data['rating'],
            feedbacks=data['feedbacks'],
            colors=data['colors'][0]['name'] if data['colors'] else None
        )

        conn.execute(ins)
        return f"Товар '{data['name']}' добавлен в базу данных"
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
