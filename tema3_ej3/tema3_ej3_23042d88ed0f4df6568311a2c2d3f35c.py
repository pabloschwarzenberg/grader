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
cuenta = CuentaCorriente("12345678-9", 50000)
print("Saldo inicial:", cuenta.saldo)

monto_a_girar = 30000
if cuenta.girar(monto_a_girar):
    print("Giro exitoso de", monto_a_girar)
else:
    print("Saldo insuficiente para realizar el giro")

print("Saldo actual:", cuenta.saldo)
