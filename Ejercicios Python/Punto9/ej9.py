class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print("Deposito exitoso")
        else:
            print("Monto Invalido")

    def retirar(self, monto):
        if 0 < monto: 
            if monto <= self.__saldo:
                self.__saldo -= monto
                print("Retiro Exitoso")
            else:
                print("Saldo Insuficiente")
        else:
            print("Monto Invalido")

    def mostrarInfo(self):
        print(f"Titular: {self.titular} | Saldo: ${self.__saldo}")

def main():
    c1 = CuentaBancaria("Thiago Brunt")
    c2 = CuentaBancaria("Leo Messi", 10000000)

    print("Cuentas antes de las operaciones:")
    c1.mostrarInfo()
    c2.mostrarInfo()
    print(" ")

    c1.depositar(-10)
    c1.depositar(10000)

    c2.retirar(-10)
    c2.retirar(280000)

    c1.retirar(-10)
    c1.retirar(200000)

    print(" ")
    print("Cuentas despues de las operaciones:")
    c1.mostrarInfo()
    c2.mostrarInfo()

if __name__ == "__main__":
    main()