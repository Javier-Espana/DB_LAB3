from sqlalchemy import create_engine, MetaData, Column, Integer, String, Date, DateTime, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.schema import CreateTable, DDLElement
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import re

Base = declarative_base()

class TipoCarnet(String):
    def __init__(self):
        super().__init__(10)
    
    @property
    def python_type(self):
        return str

class TipoEstadoInscripcion(ENUM):
    def __init__(self):
        super().__init__('activo', 'inactivo', name='estado_inscripcion')

class Estudiante(Base):
    __tablename__ = 'estudiantes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    fecha_nacimiento = Column(Date, nullable=False)
    carnet = Column(TipoCarnet(), nullable=False, unique=True)
    creado_en = Column(DateTime, server_default=func.now())

class Curso(Base):
    __tablename__ = 'cursos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(20), nullable=False, unique=True)
    horario = Column(String(50), nullable=False)
    aula = Column(String(10), nullable=False)
    creado_en = Column(DateTime, server_default=func.now())

class Inscripcion(Base):
    __tablename__ = 'inscripciones'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id', ondelete='CASCADE'), nullable=False)
    curso_id = Column(Integer, ForeignKey('cursos.id', ondelete='CASCADE'), nullable=False)
    fecha_inscripcion = Column(DateTime, server_default=func.now())
    estado = Column(TipoEstadoInscripcion(), nullable=False)

def generar_schema(url_bd='postgresql://usuario:contraseña@localhost/basedatos'):
    """Genera el archivo schema.sql con todo el DDL necesario"""
    
    motor = create_engine(url_bd)
    metadatos = Base.metadata
    
    sentencias_ddl = []
    
    sentencias_ddl.append("""
    -- Tipos personalizados
    CREATE TYPE estado_inscripcion AS ENUM ('activo', 'inactivo');
    """)
    
    for tabla in metadatos.sorted_tables:
        sentencias_ddl.append(str(CreateTable(tabla).compile(motor)))
    
    sentencias_ddl.append("""
    -- Restricción para formato de carnet (A-XXXX-YYYY)
    ALTER TABLE estudiantes
    ADD CONSTRAINT chk_formato_carnet 
    CHECK (carnet ~ '^A-\\d{4}-\\d{4}$');
    """)
    
    sentencias_ddl.append("""
    -- Restricción para edad mínima (16 años)
    ALTER TABLE estudiantes
    ADD CONSTRAINT chk_edad_minima
    CHECK (fecha_nacimiento <= CURRENT_DATE - INTERVAL '16 years');
    """)
    
    sentencias_ddl.append("""
    -- Vista para relación estudiantes-cursos
    CREATE OR REPLACE VIEW vista_estudiantes_cursos AS
    SELECT 
        e.nombre AS estudiante,
        e.carnet,
        c.nombre AS curso,
        c.codigo,
        i.fecha_inscripcion,
        i.estado
    FROM inscripciones i
    JOIN estudiantes e ON i.estudiante_id = e.id
    JOIN cursos c ON i.curso_id = c.id;
    """)
    
    with open('schema.sql', 'w', encoding='utf-8') as archivo:
        archivo.write("-- Script DDL generado automáticamente el {}\n\n".format(datetime.now()))
        archivo.write("\n\n".join(sentencias_ddl))
    
    print("¡Archivo schema.sql generado con éxito!")

