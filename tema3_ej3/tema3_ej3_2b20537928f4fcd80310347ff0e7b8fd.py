class CuentaCorriente:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        else:
            return False

cuenta = CuentaCorriente("123456789", 1000)

if cuenta.girar(500):
    print("Giro realizado correctamente")
else:
    print("Fondos insuficientes")

if cuenta.girar(1000):
    print("Giro realizado correctamente")
else:
    print("Fondos insuficientes")
