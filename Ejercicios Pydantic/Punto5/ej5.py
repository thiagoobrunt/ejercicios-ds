from pydantic import BaseModel, HttpUrl, Field, ValidationError
from typing import Annotated, Optional, Union

RedSocial = Union[HttpUrl, str]

class PerfilUsuario(BaseModel):
    username: Annotated[str, Field(pattern=r"^[a-z0-9_]{3,20}$")]

    biografia : Optional[str] = Field(default=None, max_length=200)

    redes_sociales : Optional[list[RedSocial]] = Field(default_factory=list)

def main():
    p1 = PerfilUsuario(username="thiagoo10")
    print(f"{p1}")

    try:
        p1.redes_sociales.append("https//google.com")
        p1.redes_sociales.append("https//instagram")
    except ValidationError as error:
        print(f"{error}")

    print(f"{p1}")

if __name__ == "__main__":
    main()