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

# Ejemplo de uso
cuenta = CuentaCorriente("123456789", 10000)

# Realizar un giro de $5000
if cuenta.girar(5000):
    print("Giro realizado.")
else:
    print("Saldo insuficiente.")

# Realizar un giro de $15000
if cuenta.girar(15000):
    print("Giro realizado.")
else:
    print("Saldo insuficiente.")

print("Saldo actual:", cuenta.saldo)
