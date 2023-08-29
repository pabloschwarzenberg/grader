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
cuenta_1 = Cuenta("12864303-6", 10000)
puede_girar = cuenta_1.girar(500)
if puede_girar:
    print("Giro realizado correctamente.")
else:
    print("No se puede realizar el giro.")
print("Saldo actual:", cuenta_1.saldo)
