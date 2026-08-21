from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing_extensions import Annotated

class UsuarioSistema(BaseModel):
    email : EmailStr
    nivel_acceso : Annotated[int, Field(ge=1, le=5)]

def main():
    try:
        u1 = UsuarioSistema(email=234, nivel_acceso=34)
        print("Creado")
    except ValidationError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()