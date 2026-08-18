def main():
    try:
        costoPasaje = input("Ingrese el costo del pasaje: ")
        costoAlojamiento = input("Ingrese el costo de alojamiento: ")
        cantNoches = input("Ingrese la cantidad de Noches del viaje: ")
        dineroDisp = input("Ingrese la cantidad de dinero disponible: ")
        costoTotal = float(costoPasaje) + (float(costoAlojamiento) * int(cantNoches))
        dineroSuficiente = float(costoTotal) < float(dineroDisp)
        print(f"Pasaje: ${costoPasaje}, Alojamiento: ${costoAlojamiento}, CantNoches: {cantNoches}, Dinero Disponible: ${dineroDisp}")
        print(f"Costo total del viaje: ${costoTotal}")
        if dineroSuficiente:
            print("Se puede realizar viaje, dinero suficiente")
        else:
            print("No se puede realizar el viaje, dinero insuficiente")    
    except ValueError:
        print("Ingrese un número válido.")

if __name__ == "__main__":
    main()