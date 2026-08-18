from biblioteca.Modelos.libro import Libro 
import biblioteca.Servicios.prestamo as prestamo

def main():
    l1 = Libro("Padre Rico, Padre Pobre", "Robert Kiyosaki")
    l2 = Libro("Harry Potter", "J.K. Rowling", False)

    prestamo.consultarDisponibilidad(l1)
    prestamo.realizarPrestamo(l1)
    prestamo.consultarDisponibilidad(l1)

    prestamo.realizarPrestamo(l2)
    prestamo.consultarDisponibilidad(l2)
    prestamo.realizarDevolucion(l2)

    prestamo.realizarDevolucion(l2)

if __name__ == "__main__":
    main()