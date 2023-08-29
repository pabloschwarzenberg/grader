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
cuenta_1 = CuentaCorriente("12864303-6", 10000)
print("Saldo inicial de cuenta_1:", cuenta_1.saldo)

monto_giro = 5000
puede_girar = cuenta_1.girar(monto_giro)
if puede_girar:
    print("Se realizó un giro de", monto_giro)
else:
    print("No se pudo realizar el giro de", monto_giro)

print("Saldo actual de cuenta_1:", cuenta_1.saldo)
