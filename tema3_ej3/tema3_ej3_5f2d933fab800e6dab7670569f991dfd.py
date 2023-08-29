class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False


if __name__ == "__main__":
    cuenta = Cuenta("12345678-9", 50000)
    print(cuenta.girar(20000))
    print(cuenta.saldo)
    print(cuenta.girar(40000))
    print(cuenta.saldo)

           