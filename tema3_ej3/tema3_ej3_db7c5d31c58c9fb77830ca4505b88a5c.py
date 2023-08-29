class CuentaCorriente:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        else:
            return False

# Crear una instancia de la clase CuentaCorriente
cuenta_1 = CuentaCorriente("12864303-6", 10000)

# Realizar un giro de 500
puede_girar = cuenta_1.girar(500)
if puede_girar:
    print("Giro exitoso. Nuevo saldo:", cuenta_1.saldo)
else:
    print("No se puede realizar el giro. Saldo insuficiente.")

# Realizar un giro de 1000
puede_girar = cuenta_1.girar(1000)
if puede_girar:
    print("Giro exitoso. Nuevo saldo:", cuenta_1.saldo)
else:
    print("No se puede realizar el giro. Saldo insuficiente.")
