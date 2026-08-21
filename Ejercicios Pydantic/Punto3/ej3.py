from typing import Annotated, Optional
from pydantic import BaseModel, Field

CoordenadasGPS = Annotated[float, Field(ge=-90, le=90)]

class Ubicacion(BaseModel):
    longitud : CoordenadasGPS
    latitud : CoordenadasGPS
    etiqueta : Optional[str] = None

def main():
    u1 = Ubicacion(longitud=80, latitud=-20)
    print(f"Ubicacion {u1}")
    u2 = Ubicacion(longitud=30, latitud=20, etiqueta="Cancha de Fútbol")
    print(f"Ubicacion {u2}")

    try:
        u3 = Ubicacion(longitud=-100, latitud=-20)
    except:
        print("Error de longitud")

    try:
        u4 = Ubicacion(longitud=90, latitud=200)
    except:
        print("Error de latitud")

if __name__ == "__main__":
    main()