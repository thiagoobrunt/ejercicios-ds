def analizar_temperaturas(registros):
    promedio = 0
    for i in registros:
        promedio = promedio + i
    promedio = promedio / (len(registros))
    minimo = min(registros)
    maximo = max(registros)
    return (minimo,maximo,promedio)

def main():
    temperaturas = (10, 5, 1.6, 3, 7, -2, 9.5)
    minimo, maximo, promedio = analizar_temperaturas(temperaturas)
    print(f"La temperatura minima fue {minimo} grados\n" \
          f"La maxima fue {maximo} grados\n" \
          f"Y la temperatura promedio es de {promedio} grados")

if __name__ == "__main__":
    main()