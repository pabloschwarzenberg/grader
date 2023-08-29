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
    cuenta = Cuenta("12345678-9", 10000)
    print(cuenta.girar(5000))  # True, se puede girar 5000 pesos
    print(cuenta.saldo)  # 5000, saldo actualizado
    print(cuenta.girar(10000))  # False, no se puede girar 10000 pesos (saldo insuficiente)
    print(cuenta.saldo)  # 5000, saldo no se ha modificado