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

# Ejemplo de uso
cuenta = CuentaCorriente("123456789", 1000000)
print("Saldo inicial:", cuenta.saldo)

monto_giro = 500000
if cuenta.girar(monto_giro):
    print("Giro realizado. Nuevo saldo:", cuenta.saldo)
else:
    print("No se puede realizar el giro. Saldo insuficiente.")

