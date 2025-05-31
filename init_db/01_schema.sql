-- Script DDL generado automáticamente el 2025-05-31 06:37:41.186448


    -- Tipos personalizados
    DO $$ BEGIN
        IF EXISTS (SELECT 1 FROM pg_type WHERE typname = 'estado_inscripcion') THEN
            DROP TYPE estado_inscripcion CASCADE;
        END IF;
    END $$;
    CREATE TYPE estado_inscripcion AS ENUM ('activo', 'inactivo');
    


CREATE TABLE cursos (
	id SERIAL NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	codigo VARCHAR(20) NOT NULL, 
	horario VARCHAR(50) NOT NULL, 
	aula VARCHAR(10) NOT NULL, 
	creado_en TIMESTAMP WITHOUT TIME ZONE DEFAULT now(), 
	PRIMARY KEY (id), 
	UNIQUE (codigo)
)

;


CREATE TABLE estudiantes (
	id SERIAL NOT NULL, 
	nombre VARCHAR(100) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
	fecha_nacimiento DATE NOT NULL, 
	carnet VARCHAR(11) NOT NULL, 
	creado_en TIMESTAMP WITHOUT TIME ZONE DEFAULT now(), 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (carnet)
)

;


CREATE TABLE inscripciones (
	id SERIAL NOT NULL, 
	estudiante_id INTEGER NOT NULL, 
	curso_id INTEGER NOT NULL, 
	fecha_inscripcion TIMESTAMP WITHOUT TIME ZONE DEFAULT now(), 
	estado estado_inscripcion NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(estudiante_id) REFERENCES estudiantes (id) ON DELETE CASCADE, 
	FOREIGN KEY(curso_id) REFERENCES cursos (id) ON DELETE CASCADE
)

;


    -- Restricción para formato de carnet (A-XXXX-YYYY)
    ALTER TABLE estudiantes
    ADD CONSTRAINT chk_formato_carnet 
    CHECK (carnet ~ '^A-\d{4}-\d{4}$');
    


    -- Restricción para edad mínima (16 años)
    ALTER TABLE estudiantes
    ADD CONSTRAINT chk_edad_minima
    CHECK (fecha_nacimiento <= CURRENT_DATE - INTERVAL '16 years');
    


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
    