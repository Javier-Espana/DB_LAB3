from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

Base = declarative_base()

# ----------------------------
# Tipos Personalizados
# ----------------------------

# Tipo 1: Estado de inscripción (ENUM)
class EstadoInscripcion(PyEnum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"

# Tipo 2: Validación de formato de carnet (A-XXXX-YYYY)
def validar_formato_carnet(carnet: str) -> bool:
    """Valida que el carnet cumpla con el formato A-XXXX-YYYY"""
    import re
    return re.match(r'^A-\d{4}-\d{4}$', carnet) is not None

# ----------------------------
# Modelos de Base de Datos
# ----------------------------

class Estudiante(Base):
    _tablename_ = 'estudiantes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    fecha_nacimiento = Column(Date, nullable=False)
    carnet = Column(String(10), nullable=False, unique=True)  # Validación se hará a nivel de aplicación/BD
    
    # Relación con cursos a través de inscripciones
    inscripciones = relationship("Inscripcion", back_populates="estudiante", cascade="all, delete-orphan")

class Curso(Base):
    _tablename_ = 'cursos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(20), nullable=False, unique=True)
    horario = Column(String(50))
    aula = Column(String(10))
    
    # Relación con estudiantes
    inscripciones = relationship("Inscripcion", back_populates="curso")

class Inscripcion(Base):
    _tablename_ = 'inscripciones'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id', ondelete="CASCADE"), nullable=False)
    curso_id = Column(Integer, ForeignKey('cursos.id', ondelete="CASCADE"), nullable=False)
    estado = Column(Enum(EstadoInscripcion), nullable=False)
    fecha_inscripcion = Column(Date, server_default="CURRENT_DATE")
    
    # Relaciones
    estudiante = relationship("Estudiante", back_populates="inscripciones")
    curso = relationship("Curso", back_populates="inscripciones")