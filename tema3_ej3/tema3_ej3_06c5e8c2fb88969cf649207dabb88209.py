from cuenta import Cuenta

class CuentaCorriente:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False

cuenta_1 = CuentaCorriente("12864303-6", 10000)
monto_giro = 500

if cuenta_1.girar(monto_giro):
    print("Giro exitoso. Nuevo saldo:", cuenta_1.saldo)
else:
    print("No se puede realizar el giro. Saldo insuficiente.")
