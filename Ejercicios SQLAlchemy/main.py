from datetime import datetime
from database import Base, SessionLocal, engine
from models import Profesor, Departamento, Curso, Clase, Estudiante, Inscripcion
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

def inscribirAlumno(db, est : Estudiante, cur : Curso):
    try:
        nuevaInscripcion = Inscripcion(estudiante=est, curso=cur)
        db.add(nuevaInscripcion)
        db.commit()  # Intenta guardar en la BD
        db.refresh(nuevaInscripcion)
        print(
            f"Matrícula exitosa: {est.nombre} inscripto en '{cur.titulo}'."
        )
    except IntegrityError as e:
        db.rollback()  # Deshace los cambios pendientes ante error de integridad
        print(
            f"El alumno {est.nombre} ya está inscripto en '{cur.titulo}'. Se ejecutó rollback()."
        )

    except Exception as e:
        db.rollback()  # Deshace cualquier otro error no esperado
        print(f"❌ Error inesperado: {e}. Se ejecutó rollback().")
    

def main():
    # 1. Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)

    # 2. Abrir sesión para interactuar con la BD
    with SessionLocal() as db:
        """
        Punto1:
        # Instanciar profesores de prueba
        p1 = Profesor(
            nombre="Carlos Gómez",
            email="carlos.gomez@unlp.edu.ar",
            fechaIngreso=datetime(2021, 3, 15, 8, 30),
        )
        p2 = Profesor(
            nombre="Mariana López",
            email="mariana.lopez@unlp.edu.ar",
        )

        # 3. Insertar registros
        db.add_all([p1, p2])
        db.commit()
        """
        """
        Punto2:
        # 1. Crear los departamentos
        depto_sistemas = Departamento(nombre="Sistemas")
        depto_matematica = Departamento(nombre="Matemática")

        # 2. Buscar a los profesores existentes en la BD
        p1 = db.query(Profesor).filter(Profesor.nombre == "Carlos Gómez").first()
        p2 = (db.query(Profesor).filter(Profesor.nombre == "Mariana López").first())

        # 3. Asignar los profesores a la lista del departamento
        if p1:
            depto_sistemas.profesores.append(p1)
        if p2:
            depto_matematica.profesores.append(p2)

        # 4. Guardar los nuevos departamentos
        db.add_all([depto_sistemas, depto_matematica])
        db.commit()

        print("Profesores asignados correctamente")

        # 4. Consultar y mostrar por consola
        profesores = db.query(Profesor).all()


        print("\n--- Lista de Profesores ---")
        for profe in profesores:
            print(profe)


        departamentos = db.query(Departamento).all()
        print("\n--- Departamentos ---")
        for depa in departamentos:
            print(depa)
            print("Dueños:\n")
            for p in depa.profesores:
                print(p)
        """
        """
        #Punto3:
        # 1. Crear el departamento y los 3 profesores
        depto = Departamento(nombre="Informática")

        p1 = Profesor(nombre="Alan Turing", email="alan@unlp.edu.ar")
        p2 = Profesor(nombre="Ada Lovelace", email="ada@unlp.edu.ar")
        p3 = Profesor(nombre="Grace Hopper", email="grace@unlp.edu.ar")

        # 2. Asociar los profesores al departamento
        depto.profesores.extend([p1, p2, p3])

        db.add(depto)
        db.commit()

        
        # 3. VERIFICACIÓN 1: Sentido Departamento -> Profesores
        depto_recuperado = (db.query(Departamento).filter_by(nombre="Informática").first())

        print(f"\n--- Departamento: {depto_recuperado.nombre} ---")
        for profe in depto_recuperado.profesores:
            print(f"Profesor del depto: {profe.nombre}")


        # 4. VERIFICACIÓN 2: Sentido Profesor -> Departamento
        profesor_recuperado = (db.query(Profesor).filter_by(nombre="Ada Lovelace").first())
        
        print("\n--- Navegación inversa desde el profesor ---")
        print(f"Profesor: {profesor_recuperado.nombre}")
        print(f"Pertenece a: {profesor_recuperado.departamento.nombre}")
        """
        """
        #punto5:
        # 1. Obtener o crear el profesor responsable
        profe = db.query(Profesor).first()
        if not profe:
            profe = Profesor(nombre="Ada Lovelace", email="ada@unlp.edu.ar")
            db.add(profe)
            db.commit()

        # 2. Instanciar el curso
        curso_algoritmos = Curso(
            titulo="Algoritmos y Estructuras de Datos",
            creditos=6,
            profesor_id=profe.id,
        )

        # 3. Instanciar las clases
        clase1 = Clase(
            tema="Introducción y Complejidad", duracionMinutos=90
        )
        clase2 = Clase(
            tema="Listas, Pilas y Colas", duracionMinutos=120
        )
        clase3 = Clase(tema="Árboles Binarios", duracionMinutos=90)

        # 4. Asociar las clases al curso mediante la relación
        curso_algoritmos.clases.extend([clase1, clase2, clase3])

        # 5. Guardar todo en la base de datos
        db.add(curso_algoritmos)
        db.commit()

        # 6. CONSULTA ORM: Obtener todas las clases del curso
        curso_buscado = (
            db.query(Curso)
            .filter_by(titulo="Algoritmos y Estructuras de Datos")
            .first()
        )

        if curso_buscado:
            print(f"\nCurso: {curso_buscado.titulo} (Profesor: {curso_buscado.profesor.nombre})")
            print(f"Total de clases: {len(curso_buscado.clases)}")
            for c in curso_buscado.clases:
                print(f"  • {c.tema} - {c.duracionMinutos} min")
        """
        """
        #Punto 7:
        # Busco Profesor
        profe = db.query(Profesor).first()
        if not profe:
            profe = Profesor(nombre="Ada Lovelace", email="ada@unlp.edu.ar")
            db.add(profe)
            db.commit()
        # Creo un curso y un estudiante
        est = Estudiante(nombre="Thiago Brunt", legajo="0002")
        cur = Curso(titulo="Bases de Datos", creditos=4,profesor_id=profe.id)

        # Inscribir pasando datos extras
        inscripcion = Inscripcion(estudiante=est,curso=cur)

        db.add(inscripcion)
        db.commit()

        # Consultar la nota desde el estudiante
        alumno = db.query(Estudiante).first()
        for insc in alumno.inscripciones:
            print(
                f"Alumno: {alumno.nombre} | Materia: {insc.curso.titulo} | Nota: {insc.calificacionFinal} | Fecha: {insc.fechaInscripcion}"
            )
        """
        """
        #punto 8
        # Consulta usando join explícito
        cursosProfe = (
            db.query(Curso)
            .join(Curso.profesor)
            .filter(Profesor.nombre == "Alan Turing")
            .all()
        )

        print("\n--- Cursos dictados por Alan Turing ---")
        for curso in cursosProfe:
            print(f"Curso: {curso.titulo} | Créditos: {curso.creditos}")

        # Consulta del promedio (usando el legajo o estudianteId)

        resultado = (
            db.query(func.avg(Inscripcion.calificacionFinal))
            .filter(Inscripcion.estudianteId == 1)  
            .scalar()
        )  

        promedio = resultado if resultado is not None else 0.0
        print(f"\nPromedio del estudiante: {promedio:.2f}")

        # Contar alumnos por cada curso
        reporteCursos = (
            db.query(
                Curso.titulo,
                func.count(Inscripcion.estudianteId).label("totalAlumnos"),
            )
            .outerjoin(Curso.inscripciones)
            .group_by(Curso.id, Curso.titulo)
            .all()
        )

        print("\n--- Cantidad de alumnos por curso ---")
        for titulo, total in reporteCursos:
            print(f"Curso: {titulo} | Inscriptos: {total}")
        """

        #punto 9:
        estudiante = db.query(Estudiante).first()
        curso = db.query(Curso).first()

        #Primera vez que inscribo
        inscribirAlumno(db, estudiante, curso)

        #Segunda vez con mismos parametros para forzar error:
        inscribirAlumno(db, estudiante, curso)

        # Verificación manual del rollback en la base de datos
        totalInscripciones = (
            db.query(Inscripcion)
            .filter_by(estudianteId=estudiante.id, cursoId=curso.id)
            .count()
        )

        print(
            f"\nVerificación en BD: Cantidad de registros para este alumno en este curso = {totalInscripciones}"
        )
        

if __name__ == "__main__":
    main()