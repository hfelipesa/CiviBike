from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal
from model import bike_model as models
from schemas import bike_schemas as schemas

router = APIRouter(
    prefix="/bikes",
    tags=["bikes"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.BikeResponse)
def create_bike(bike: schemas.BikeCreate, db: Session = Depends(get_db)):
    new_bike = models.Bike(**bike.dict())
    db.add(new_bike)
    db.commit()
    db.refresh(new_bike)
    return new_bike


@router.get("/", response_model=list[schemas.BikeResponse])
def get_bikes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    bikes = db.query(models.Bike).offset(skip).limit(limit).all()
    return bikes

# Obtener una bicicleta por ID
@router.get("/{bike_id}", response_model=schemas.BikeResponse)
def get_bike(bike_id: int, db: Session = Depends(get_db)):
    bike = db.query(models.Bike).filter(models.Bike.id == bike_id).first()
    if not bike:
        raise HTTPException(status_code=404, detail="Bicicleta no encontrada")
    return bike
