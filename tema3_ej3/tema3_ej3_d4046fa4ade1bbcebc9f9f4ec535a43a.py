class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        else:
            return False


if __name__ == "__main__":
    cuenta = Cuenta("123456789", 1000)
    print(cuenta.girar(500))  # True
    print(cuenta.saldo)  # 500
    print(cuenta.girar(1000))  # False
    print(cuenta.saldo)  # 500
