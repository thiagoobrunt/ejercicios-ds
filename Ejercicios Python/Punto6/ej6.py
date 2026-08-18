def main():
    opcion = ""
    while opcion != "c":
        opcion = input("Elija una opcion:\n" \
        "a) Calcular la suma de los primeros N números naturales\n" \
        "b) Encontrar todos los números divisibles por 3 en un rango\n" \
        "c) Salir\n")

        match opcion:
            case "a":
                try:
                    n = int(input("Ingrese N(Número entero positivo): "))
                    suma = 0
                    if n <= 0:
                        raise ValueError
                    for i in range(1, n + 1):
                        suma += i
                    print(f"El valor de la suma es de: {suma}\n")
                except ValueError:
                    print("Ingrese un valor válido\n")
            case "b":
                try:
                    a = int(input("Ingrese el valor menor del rango: "))
                    b = int(input("Ingrese el valor mayor del rango: "))
                    if a >= b:
                        raise ValueError
                    print("Números divisibles por 3 dentro del rango:")
                    for i in range(a, b):
                        if (i % 3) == 0:
                            print(f"{i}")
                except ValueError:
                    print("Ingrese un valor válido\n")
            case "c":
                print("Saliendo...")
            case _:
                print("Ingrese una opcion válida\n")

if __name__ == "__main__":
    main()