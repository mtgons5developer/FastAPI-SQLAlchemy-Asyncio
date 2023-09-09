from fastapi import FastAPI
from async_firestore_sqlalchemy import AsyncFirestoreSQLAlchemy
import asyncio

app = FastAPI()

# SQLAlchemy Configuration
db = AsyncFirestoreSQLAlchemy(
    database_url='your_firestore_credentials.json',  # Replace with your Firestore credentials JSON file
    echo=True  # Set to True for debugging, False for production
)

# SQLAlchemy Model
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

# Create database tables
@app.on_event("startup")
async def startup_db():
    await db.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await db.disconnect()

# FastAPI Endpoints
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    async with db.transaction():
        new_item = Item(**item.dict())
        db.session.add(new_item)
        await db.session.commit()
        await db.session.refresh(new_item)
        return new_item

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    item = await db.session.query(Item).filter_by(id=item_id).first()
    if item:
        return item
    else:
        return {"error": "Item not found"}

@app.get("/items/", response_model=list[Item])
async def read_items():
    items = await db.session.query(Item).all()
    return items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
