from ..Modelos.libro import Libro

def realizarPrestamo(libro : Libro):
    if libro.disponible:
        libro.disponible = False
        print(f"Se realizó el prestamo del libro {libro.titulo} con éxito\n")
    else:
        print(f"El Libro {libro.titulo} ya se encuentra prestado\n")

def realizarDevolucion(libro: Libro):
    if not libro.disponible:
        libro.disponible = True
        print(f"Se realizó la devolución del libro {libro.titulo} con éxito\n")
    else:
        print(f"El libro {libro.titulo} ya figura como disponible\n")

def consultarDisponibilidad(libro: Libro):
    if libro.disponible:
        print(f"El libro {libro.titulo} se encuentra disponible\n")
    else:
        print(f"El libro {libro.titulo} no se encuentra disponible\n")