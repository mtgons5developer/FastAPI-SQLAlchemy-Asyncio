from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

Base = declarative_base()

class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    carbon_emission = Column(Integer, nullable=False)

class BuildingRequest(BaseModel):
    name: str
    carbon_emission: int

class BuildingResponse(BaseModel):
    id: int
    name: str
    carbon_emission: int

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.post("/buildings/", response_model=BuildingResponse)
def create_building(building: BuildingRequest):
    db = SessionLocal()
    db_building = Building(**building.dict())
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    db.close()
    return db_building

@app.get("/buildings/{building_id}", response_model=BuildingResponse)
def read_building(building_id: int):
    db = SessionLocal()
    building = db.query(Building).filter(Building.id == building_id).first()
    db.close()
    if building is None:
        raise HTTPException(status_code=404, detail="Building not found")
    return BuildingResponse(**building.__dict__)

def initialize_db():
    db = SessionLocal()
    db.execute(text("PRAGMA foreign_keys=1"))
    Base.metadata.create_all(bind=engine)
    db.close()

initialize_db()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
