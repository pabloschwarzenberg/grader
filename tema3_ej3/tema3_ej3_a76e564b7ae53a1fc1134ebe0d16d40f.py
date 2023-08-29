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

cuenta_1 = Cuenta("12864303-6", 10000)
print(cuenta_1.girar(500))  # True
print(cuenta_1.saldo)  # 9500

print(cuenta_1.girar(12000))  # False
print(cuenta_1.saldo)  # 9500
