from sqlalchemy import create_engine, MetaData
from datetime import datetime, timedelta
import random
from faker import Faker
import os

#configuracion inicial
fake = Faker('es_ES')
Faker.seed(42)
random.seed(42)

#funcion para generar el script data.sql
def generar_data_sql():
    #crear el contenido del archivo
    contenido = """-- Script de inserción de datos generado automáticamente
-- Fecha: {fecha_actual}
-- Total: 30 registros significativos con relaciones múltiples

""".format(fecha_actual=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    #1.-generar 10 estudiantes
    estudiantes = []
    for i in range(1, 11):
        año_actual = datetime.now().year
        carnet = f"A-{random.randint(1000, 9999)}-{año_actual}"
        fecha_nac = fake.date_of_birth(minimum_age=16, maximum_age=30)
        
        estudiantes.append((i, carnet))
        contenido += f"INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (\n"
        contenido += f"  {i},\n"
        contenido += f"  '{fake.name()}',\n"
        contenido += f"  '{fake.unique.email()}',\n"
        contenido += f"  '{fecha_nac}',\n"
        contenido += f"  '{carnet}'\n"
        contenido += ");\n\n"

    #2.-generar 5 cursos
    cursos = []
    codigos_usados = set()
    for i in range(1, 6):
        while True:
            codigo = f"CC-{random.randint(100, 999)}"
            if codigo not in codigos_usados:
                codigos_usados.add(codigo)
                break
                
        cursos.append((i, codigo))
        contenido += f"INSERT INTO cursos (id, nombre, codigo, horario, aula) VALUES (\n"
        contenido += f"  {i},\n"
        contenido += f"  '{fake.catch_phrase()}',\n"
        contenido += f"  '{codigo}',\n"
        contenido += f"  '{random.choice(['L-M 10:00', 'M-J 14:00', 'V 16:00', 'S 9:00'])}',\n"
        contenido += f"  'A-{random.randint(1, 20)}'\n"
        contenido += ");\n\n"

    #3.-generar 30 inscripciones (relaciones múltiples)
    #asegurar que cada estudiante tenga al menos 2 cursos
    for est_id, _ in estudiantes:
        cursos_estudiante = random.sample(cursos, k=random.randint(2, 4))
        for curso in cursos_estudiante:
            curso_id, _ = curso
            fecha_insc = fake.date_time_between(start_date='-1y', end_date='now')
            estado = random.choice(['activo', 'inactivo'])
            
            contenido += f"INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (\n"
            contenido += f"  {est_id},\n"
            contenido += f"  {curso_id},\n"
            contenido += f"  '{fecha_insc}',\n"
            contenido += f"  '{estado}'\n"
            contenido += ");\n\n"

    #escribir el archivo
    with open('data.sql', 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    print("Archivo data.sql generado con éxito!")
    print(f"- {len(estudiantes)} estudiantes")
    print(f"- {len(cursos)} cursos")
    print("- 30 inscripciones (relaciones múltiples)")

if _name_ == "_main_":
    generar_data_sql()