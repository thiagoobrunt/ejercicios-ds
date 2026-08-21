from pydantic import BaseModel
from typing import Union, Literal

TIPO = Literal["Sensor", "Actuador", "Gateway"]

class Dispositivo(BaseModel):
    id_dispositivo : Union[int, str]
    tipo: TIPO

def main():
    d1 = Dispositivo(id_dispositivo=123, tipo="Sensor")
    print("d1 creado")
    d2 = Dispositivo(id_dispositivo="1234", tipo="Actuador")
    print("d2 creado")

    try:
        d3 = Dispositivo(id_dispositivo=2.2, tipo="Sensor")
    except:
        print("Error de id")

    try:
        d4 = Dispositivo(id_dispositivo=2, tipo="sistema")
    except:
        print("Error de tipo")

if __name__ == "__main__":
    main()