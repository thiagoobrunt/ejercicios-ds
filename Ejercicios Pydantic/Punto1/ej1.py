from pydantic import BaseModel, Field, EmailStr
from typing_extensions import Annotated

class Estudiante(BaseModel):
    legajo : Annotated[int, Field(gt=0)]
    nombreCompleto : Annotated[str, Field(min_length=5, max_length=30)]
    email: EmailStr
    promedio: Annotated[float, Field(default=0.0, ge=0.0, le=10.0)]

def main():
    try:
        e1 = Estudiante(legajo=-2,nombreCompleto="thiago", email="thiago@gmail.com")
    except:
        print("Fallo por el legajo")

    try:
        e2 = Estudiante(legajo=1234, nombreCompleto="th", email="email@gma.com")
    except:
        print("Fallo por el nombre")

    try:
        e3 = Estudiante(legajo=123, nombreCompleto="thiago", email=efiejf)
    except:
        print("Fallo por Email")

    try:
        e4 = Estudiante(legajo=123, nombreCompleto="thiagp", email="thia@gma.com", promedio=20)
    except:
        print("Fallo Por promedio")

if __name__ == "__main__":
    main()