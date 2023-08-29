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
    cuenta_1 = Cuenta("12864303-6", 10000)
    print(cuenta_1.girar(5000))  # Output: True
    print(cuenta_1.saldo)  # Output: 5000
    print(cuenta_1.girar(10000))  # Output: False
    print(cuenta_1.saldo)  # Output: 5000 (saldo no se modificó)
