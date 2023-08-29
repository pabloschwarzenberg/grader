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

puede_girar = cuenta_1.girar(5000)
if puede_girar:
    print("Giro exitoso. Nuevo saldo:", cuenta_1.saldo)
else:
    print("No es posible realizar el giro. Saldo insuficiente.")

puede_girar = cuenta_1.girar(10000)
if puede_girar:
    print("Giro exitoso. Nuevo saldo:", cuenta_1.saldo)
else:
    print("No es posible realizar el giro. Saldo insuficiente.")

