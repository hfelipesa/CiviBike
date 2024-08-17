from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal
from model import user_model as models
from schemas import user_schemas as schemas


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")
    
    new_user = models.User(**user.dict())  # Convierte el esquema Pydantic a un diccionario para crear un nuevo modelo
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=list[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


@router.get("/{id_document}", response_model=schemas.UserResponse)
def get_user(id_document: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id_document == id_document).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
