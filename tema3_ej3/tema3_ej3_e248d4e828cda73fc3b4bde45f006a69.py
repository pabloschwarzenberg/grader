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

# Crear una instancia de CuentaCorriente
cuenta_1 = CuentaCorriente("12864303-6", 10000)

# Ejemplo de uso
monto_a_girar = 5000
puede_girar = cuenta_1.girar(monto_a_girar)

if puede_girar:
    print("Se realizó el giro de", monto_a_girar)
else:
    print("No se puede realizar el giro de", monto_a_girar)
