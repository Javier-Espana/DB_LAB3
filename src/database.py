from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

#configuracion de la conexion a db
DATABASE_URL = "postgresql://user:pass@localhost/lab3_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#funcion para obtener la sesión de db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)