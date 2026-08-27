from datetime import datetime
from sqlalchemy import DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import Optional

class Profesor(Base):
    __tablename__ = "profesores"
    id : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(30))
    email : Mapped[str] = mapped_column(String(50))
    fechaIngreso : Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    departamento_id : Mapped[Optional[int]] = mapped_column(ForeignKey("departamentos.id"), default=None)

    departamento : Mapped[Optional["Departamento"]] = relationship(back_populates="profesores")

    cursos : Mapped[list["Curso"]] = relationship(back_populates="profesor")

    def __repr__(self) -> str:
        return f"<Profesor(id={self.id}, nombre='{self.nombre}', email='{self.email}', ingreso={self.fechaIngreso})>"


class Departamento(Base):
    __tablename__ = "departamentos"

    id : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(40))

    profesores: Mapped[list["Profesor"]] = relationship(back_populates="departamento")

    def __repr__(self) -> str:
        return f"<Departamento(id={self.id}, nombre='{self.nombre}')>"

class Curso(Base):
    __tablename__ = "cursos"

    id : Mapped[int] = mapped_column(primary_key=True)
    titulo : Mapped[str] = mapped_column(String(40))
    creditos : Mapped[int] = mapped_column(default=0)

    profesor_id : Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    profesor : Mapped[Optional["Profesor"]] = relationship(back_populates="cursos")

    clases : Mapped[list["Clase"]] = relationship(back_populates="curso")

    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="curso")

    def __repr__(self) -> str:
        return f"Curso(id={self.id}, titulo={self.titulo}, créditos={self.creditos}, profesor={self.profesor.nombre})"

class Clase(Base):
    __tablename__ = "clases"
    id : Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(30))
    duracionMinutos : Mapped[int] = mapped_column(default=0)

    cursoId : Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso : Mapped[Optional["Curso"]] = relationship(back_populates="clases")

    def __repr__(self) -> str:
        return f"Curso(id={self.id}, tema={self.tema}, Duracion: {self.duracionMinutos}minutos)"

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(40))
    legajo : Mapped[str] = mapped_column(String(20), unique=True)

    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="estudiante")

    def __repr__(self) -> str:
        return f"Estudiante {self.nombre}, id={self.id}, legajo={self.legajo}"

class Inscripcion(Base):
    __tablename__ = "inscripciones"
    estudianteId : Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    cursoId : Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)
    fechaInscripcion : Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    calificacionFinal : Mapped[Optional[float]] = mapped_column(default=None)

    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")
