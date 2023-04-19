from celery import Celery
from celery.schedules import crontab

import crud
from config import REDIS_HOST, REDIS_PORT
from database import SessionLocal

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


@celery.task
def update_product_task():
    db = SessionLocal()
    products = crud.get_all_products(db)
    print(products)
    for product in products:
        crud.update_product(db=db, nm_id=product.nm_id)
    return {'status': 'OK'}


celery.conf.beat_schedule = {
    'update-products': {
        'task': 'tasks.update_product_task',
        'schedule': crontab(hour=5, minute=30),
    },
}
