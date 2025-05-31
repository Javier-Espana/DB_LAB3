-- Script de inserción de datos generado automáticamente
-- Fecha: 2025-05-31 06:37:41
-- Total: 30 registros significativos con relaciones múltiples

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  1,
  'Raimundo Llopis Hierro',
  'emiliocalatayud@example.net',
  '2004-01-02',
  'A-2824-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  2,
  'Antonia del Antón',
  'buenoisaias@example.org',
  '2005-07-10',
  'A-1409-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  3,
  'Lisandro Flor Rivas',
  'vidallobo@example.org',
  '2001-12-28',
  'A-5506-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  4,
  'Paco Rocamora Nieto',
  'fabricio35@example.org',
  '2005-10-17',
  'A-5012-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  5,
  'Gastón Núñez Lamas',
  'segoviabrunilda@example.org',
  '1995-10-21',
  'A-4657-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  6,
  'Ani Marcos Pardo',
  'juliebanos@example.org',
  '2009-01-03',
  'A-3286-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  7,
  'Aníbal Teófilo Guerrero Cabrero',
  'dlobo@example.net',
  '2004-05-01',
  'A-2679-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  8,
  'Gil Padilla Gallego',
  'judith19@example.net',
  '2006-12-04',
  'A-9935-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  9,
  'Ceferino del Pino',
  'angela83@example.net',
  '1996-12-23',
  'A-2424-2025'
);

INSERT INTO estudiantes (id, nombre, email, fecha_nacimiento, carnet) VALUES (
  10,
  'Darío Antón Moles',
  'eleal@example.org',
  '1999-04-11',
  'A-7912-2025'
);

INSERT INTO cursos (id, nombre, codigo, horario, aula) VALUES (
  1,
  'Re-contextualized transitional functionalities',
  'CC-132',
  'L-M 10:00',
  'A-3'
);

INSERT INTO cursos (id, nombre, codigo, horario, aula) VALUES (
  2,
  'Extended solution-oriented methodology',
  'CC-323',
  'M-J 14:00',
  'A-17'
);

INSERT INTO cursos (id, nombre, codigo, horario, aula) VALUES (
  3,
  'Object-based secondary knowledgebase',
  'CC-716',
  'L-M 10:00',
  'A-18'
);

INSERT INTO cursos (id, nombre, codigo, horario, aula) VALUES (
  4,
  'Digitized empowering challenge',
  'CC-303',
  'S 9:00',
  'A-8'
);

INSERT INTO cursos (id, nombre, codigo, horario, aula) VALUES (
  5,
  'Fully-configurable value-added open architecture',
  'CC-559',
  'V 16:00',
  'A-1'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  1,
  4,
  '2024-12-13 21:24:49.040026',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  1,
  3,
  '2025-02-27 21:00:42.642664',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  2,
  3,
  '2024-11-03 12:24:58.181405',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  2,
  1,
  '2024-12-30 03:58:39.459818',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  3,
  3,
  '2024-10-10 06:02:31.207209',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  3,
  5,
  '2025-05-30 07:11:11.281999',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  4,
  4,
  '2024-07-20 13:27:03.353940',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  4,
  1,
  '2024-11-27 06:54:33.913432',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  4,
  2,
  '2025-03-03 01:52:23.018803',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  4,
  5,
  '2025-04-10 13:05:22.189183',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  5,
  2,
  '2024-07-25 20:38:18.164565',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  5,
  3,
  '2024-07-28 11:13:54.793107',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  6,
  4,
  '2025-02-03 13:48:11.007263',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  6,
  3,
  '2025-01-03 20:50:47.330825',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  7,
  3,
  '2024-10-18 13:38:45.475942',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  7,
  5,
  '2025-01-03 16:16:58.819247',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  8,
  1,
  '2024-11-17 23:40:51.743651',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  8,
  2,
  '2024-08-30 20:42:14.010938',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  8,
  3,
  '2024-12-19 02:18:48.555229',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  8,
  5,
  '2025-05-10 05:59:26.890815',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  9,
  5,
  '2025-02-03 12:04:08.982645',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  9,
  2,
  '2024-07-11 21:00:04.111676',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  9,
  3,
  '2025-04-19 04:42:40.536573',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  9,
  4,
  '2025-03-01 06:52:57.489973',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  10,
  3,
  '2025-03-07 18:13:12.296406',
  'inactivo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  10,
  1,
  '2024-10-02 06:45:52.596116',
  'activo'
);

INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (
  10,
  4,
  '2024-09-15 05:37:11.075693',
  'inactivo'
);


-- Corrección de secuencias para evitar conflictos de clave primaria
SELECT setval('estudiantes_id_seq', (SELECT MAX(id) FROM estudiantes));
SELECT setval('cursos_id_seq', (SELECT MAX(id) FROM cursos));
SELECT setval('inscripciones_id_seq', COALESCE((SELECT MAX(id) FROM inscripciones), 1));
