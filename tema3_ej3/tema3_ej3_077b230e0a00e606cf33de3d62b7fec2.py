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
# Ejemplo de uso
if __name__ == "__main__":
    cuenta = Cuenta("12345678-9", 1000000)
    print(cuenta.girar(500000))  # True (Se puede girar 500000)
    print(cuenta.saldo)  # 500000
    print(cuenta.girar(700000))  # False (No se puede girar 700000)
    print(cuenta.saldo)  # 500000
       