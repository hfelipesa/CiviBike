from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal
from model import loan_model as models
from schemas import loan_schemas as schemas

router = APIRouter(
    prefix="/loans",
    tags=["loans"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.LoanResponse)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    new_loan = models.Loan(**loan.dict())
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan


@router.get("/", response_model=list[schemas.LoanResponse])
def get_loans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    loans = db.query(models.Loan).offset(skip).limit(limit).all()
    return loans


@router.get("/{loan_id}", response_model=schemas.LoanResponse)
def get_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return loan
