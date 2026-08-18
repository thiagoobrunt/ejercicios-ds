def calcularPrecioFinal(precioBase, porcentajeDescuento=10, esVip=False):
    if ((precioBase < 0) or (porcentajeDescuento < 0)):
        raise ValueError("Los valores deben ser positivos")
    precioFinal = (precioBase - (precioBase * (porcentajeDescuento/100)))
    if esVip:
        precioFinal = (precioFinal - (precioFinal * (5/100)))
    return precioFinal

def main():
    try:
        print(f"Precio Final: {calcularPrecioFinal(1000, -10,)}")
    except ValueError as error:
        print(f"{error}")

    try:
        print(f"Precio Final: {calcularPrecioFinal(-1000, 20,)}")
    except ValueError as error:
        print(f"{error}")

    try:
        print(f"Precio Final: {calcularPrecioFinal(1000, 20,)}")
        print(f"Precio Final: {calcularPrecioFinal(1000, 10, True)}")
    except ValueError as error:
        print(f"{error}")    

if __name__ == "__main__":
    main()