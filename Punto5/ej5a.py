def main():
    while True:
        contraseña = input("Ingrese una contraseña: ")

        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres\n")
        else:
            mayuscula = False
            minuscula = False
            for c in contraseña:
                if c.isupper():
                    mayuscula = True
                    break

            for c in contraseña:
                if c.islower():
                    minuscula = True
                    break
        
            if not mayuscula:
                print("La constraseña debe tener al menos una mayuscula\n")

            if not minuscula:
                print("La constraseña debe tener al menos una minuscula\n")

            if mayuscula and minuscula:
                break
            
if __name__ == "__main__":
    main()            