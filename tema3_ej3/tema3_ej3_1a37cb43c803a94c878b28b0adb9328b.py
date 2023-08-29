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
cuenta = CuentaCorriente("123456789", 1000)

# Realizar un giro de 500
if cuenta.girar(500):
    print("Giro exitoso")
else:
    print("Saldo insuficiente")

# Imprimir el saldo actual
print("Saldo actual:", cuenta.saldo)

