import streamlit as st
from models import Estudiante, Curso, Inscripcion
from database import db_session
from sqlalchemy import text
import re
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(page_title="Gestión Estudiantes", layout="wide")

# ------------------------------------------
# Validaciones (Aplicación + BD)
# ------------------------------------------
def validar_carnet(carnet):
    """Valida formato A-XXXX-YYYY"""
    return re.match(r'^A-\d{4}-\d{4}$', carnet)

def validar_edad(fecha_nac):
    edad = (datetime.now().date() - fecha_nac).days / 365
    return edad >= 16

# Limitar fecha de nacimiento a un rango razonable
hoy = datetime.now().date()
fecha_limite = hoy - timedelta(days=16*365)

# ------------------------------------------
# Vistas CRUD
# ------------------------------------------
def mostrar_estudiantes():
    """Lista principal usando la VIEW"""
    st.header("Listado de Estudiantes y Cursos")
    query = db_session.execute(text("""
        SELECT * FROM vista_estudiantes_cursos
    """)).fetchall()
    
    st.dataframe(
        query,
        column_config={
            "estudiante": "Nombre",
            "carnet": "Carnet",
            "curso": "Curso",
            "estado": st.column_config.SelectboxColumn(
                "Estado",
                options=["activo", "inactivo"]
            )
        },
        hide_index=True,
        use_container_width=True
    )

def formulario_estudiante():
    """Formulario integrado para crear/editar"""
    st.header("Registrar Nuevo Estudiante")

    # Generar carnet automáticamente (A-XXXX-YYYY)
    def generar_carnet():
        from random import randint
        año_actual = datetime.now().year
        return f"A-{randint(1000, 9999)}-{año_actual}"

    carnet_generado = generar_carnet()

    with st.form("form_estudiante"):
        nombre = st.text_input("Nombre completo")
        email = st.text_input("Email")
        fecha_nac = st.date_input(
            "Fecha de nacimiento",
            max_value=fecha_limite,
            min_value=hoy - timedelta(days=100*365)
        )
        # Mostrar carnet generado como solo lectura
        st.text_input("Carnet (generado automáticamente)", value=carnet_generado, disabled=True)

        # Selección múltiple de cursos
        cursos = db_session.query(Curso).all()
        cursos_seleccionados = st.multiselect(
            "Cursos a inscribir",
            options=[(c.id, c.nombre) for c in cursos],
            format_func=lambda x: x[1]
        )

        submitted = st.form_submit_button("Guardar")
        if submitted:
            # Validaciones de aplicación
            if not validar_carnet(carnet_generado):
                st.error("Formato de carnet inválido. Use A-XXXX-YYYY")
                return
            if not validar_edad(fecha_nac):
                st.error("El estudiante debe tener al menos 16 años")
                return

            try:
                # Crear estudiante (ORM)
                estudiante = Estudiante(
                    nombre=nombre,
                    email=email,
                    fecha_nacimiento=fecha_nac,
                    carnet=carnet_generado
                )
                db_session.add(estudiante)
                db_session.flush()  # Para obtener el ID

                # Crear inscripciones (tabla intermedia)
                for curso_id, _ in cursos_seleccionados:
                    inscripcion = Inscripcion(
                        estudiante_id=estudiante.id,
                        curso_id=curso_id,
                        estado="activo"
                    )
                    db_session.add(inscripcion)

                db_session.commit()
                st.success("Estudiante registrado con éxito!")

            except Exception as e:
                db_session.rollback()
                st.error(f"Error de base de datos: {e}")

def gestion_estudiantes():
    """Editar/Eliminar registros"""
    st.header("Gestión de Estudiantes")
    estudiantes = db_session.query(Estudiante).all()
    
    estudiante_seleccionado = st.selectbox(
        "Seleccione un estudiante",
        options=[(e.id, e.nombre) for e in estudiantes],
        format_func=lambda x: x[1]
    )
    
    if estudiante_seleccionado:
        estudiante_id, _ = estudiante_seleccionado
        estudiante = db_session.query(Estudiante).get(estudiante_id)
        
        with st.expander("Editar información"):
            with st.form(f"form_editar_{estudiante_id}"):
                nuevo_nombre = st.text_input("Nombre", value=estudiante.nombre)
                nuevo_email = st.text_input("Email", value=estudiante.email)
                
                if st.form_submit_button("Actualizar"):
                    estudiante.nombre = nuevo_nombre
                    estudiante.email = nuevo_email
                    db_session.commit()
                    st.success("Datos actualizados")
        
        if st.button("Eliminar estudiante", type="primary"):
            db_session.delete(estudiante)
            db_session.commit()
            st.success("Estudiante eliminado")

# ------------------------------------------
# Main App
# ------------------------------------------
def main():
    st.sidebar.title("Menú")
    opcion = st.sidebar.radio(
        "Seleccione una opción",
        ["Inicio", "Registrar", "Gestionar"]
    )
    
    if opcion == "Inicio":
        mostrar_estudiantes()
    elif opcion == "Registrar":
        formulario_estudiante()
    elif opcion == "Gestionar":
        gestion_estudiantes()

if __name__ == "__main__":
    main()
    db_session.close()