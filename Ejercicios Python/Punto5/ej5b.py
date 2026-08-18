def main():
    CONTRASEÑA = "Admin1234"
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese el usuario: ")

        contra = input("Ingrese la contraseña: ")

        if contra == CONTRASEÑA:
            print("Se ha ingresado con exito")
            break
        else:
            print("Contraseña incorrecta\n")
            intentos = intentos + 1

    if intentos == 3:
        print("Se bloqueo la sesión")

if __name__ == "__main__":
    main()