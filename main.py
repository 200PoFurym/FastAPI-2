from fastapi import FastAPI
from database import Base, engine
from database.userservice import get_all_users_db

# uvicorn main:app --reload
app = FastAPI(docs_url='/')
Base.metadata.create_all(bind=engine)

@app.get('/all_users', tags=['API for users'])
async def all_users():
    return get_all_users_db()

@app.post('/products', tags=['API for products'])
async def all_products(title: str, price: int):
    return {'status' : f'Your product name {title} and price {price}'}

@app.get('/example')
async def example(title: str):
    return {'message': f"Этот товар {title}"}