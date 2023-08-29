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
    cuenta_1 = Cuenta("12345678-9", 10000)
    print(cuenta_1.girar(5000))  # True
    print(cuenta_1.saldo)  # 5000
    print(cuenta_1.girar(10000))  # False
    print(cuenta_1.saldo)  # 5000