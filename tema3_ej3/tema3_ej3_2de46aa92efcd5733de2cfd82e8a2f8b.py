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
cuenta = CuentaCorriente("123456789", 5000)

print("Saldo inicial:", cuenta.saldo)
monto_giro = 3000

if cuenta.girar(monto_giro):
    print("Giro de {} realizado correctamente".format(monto_giro))
    print("Saldo actual:", cuenta.saldo)
else:
    print("No es posible realizar el giro de {}".format(monto_giro))
    print("Saldo insuficiente:", cuenta.saldo)
