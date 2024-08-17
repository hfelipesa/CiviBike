from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL="postgresql://postgres:fastApi@localhost:5432/civi_bike"

engine=create_engine(DATABASE_URL)

base=declarative_base()

SessionLocal=sessionmaker(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close() 
        

