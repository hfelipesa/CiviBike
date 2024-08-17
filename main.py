from fastapi import FastAPI
from router import user, bike, loan
from config.database import engine, base  # Importamos el motor y la base

# Instancia de la aplicación FastAPI
app = FastAPI()

# Incluimos las rutas
app.include_router(user.router)
app.include_router(bike.router)
app.include_router(loan.router)

# Crear las tablas si no existen
base.metadata.create_all(bind=engine)

# Puntos de inicio para verificar que todo esté funcionando
@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a la API de préstamos de bicicletas!"}
