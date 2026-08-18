import os


def limpiar_pantalla():
    # 'nt' es Windows, cualquier otro es Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")

def celsiusAFahrenheit(grados):
    try:
        return ((float(grados) * (9/5)) + 32)
    except ValueError:
        print("Ingrese un valor válido")

def fahrenheitACelsius(grados):
    try:
        return ((float(grados) - 32) * (5/9))
    except ValueError:
            print("Ingrese un valor válido")

def main():
    grados = input("Ingrese los grados: ")

    while True:
        i = input("Ingrese la escala\n" \
                "1) Celsius\n" \
                "2) Fahrenheit\n"
                " ")
        if ((i == "1") or (i == "2")):
            break
        print("Ingrese un número válido")

    limpiar_pantalla()

    match i:
        case "1":
            print(f"{celsiusAFahrenheit(grados)} grados Fahrenheit")
        case "2":
            print(f"{fahrenheitACelsius(grados)} grados Celsius")

if __name__ == "__main__":
    main()