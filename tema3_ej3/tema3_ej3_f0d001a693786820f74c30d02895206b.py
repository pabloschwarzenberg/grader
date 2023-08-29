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

# Realizar un giro de $500
if cuenta_1.girar(500):
    print("Giro exitoso")
    print("Nuevo saldo:", cuenta_1.saldo)
else:
    print("Saldo insuficiente")

# Realizar un giro de $1500 (monto superior al saldo actual)
if cuenta_1.girar(1500):
    print("Giro exitoso")
    print("Nuevo saldo:", cuenta_1.saldo)
else:
    print("Saldo insuficiente")
    