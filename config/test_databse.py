from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/bike"

engine = create_engine(DATABASE_URL)
Sessionlocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)

#metodo probar conexion base de datos
def test_connection():
    try:
        with engine.connect() as connection:
            print(f"Conexion exitosa a la base de datos")
    except Exception as e:
        print(f"Error de conexion: {e}")

test_connection()