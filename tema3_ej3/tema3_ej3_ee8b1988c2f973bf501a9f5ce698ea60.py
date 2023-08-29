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

# Crear una cuenta corriente con un saldo inicial de 1000 y rut "123456789"
cuenta = CuentaCorriente("123456789", 1000)

# Intentar girar 500 desde la cuenta
if cuenta.girar(500):
    print("Giro exitoso")
else:
    print("Fondos insuficientes")

# Intentar girar 1500 desde la cuenta
if cuenta.girar(1500):
    print("Giro exitoso")
else:
    print("Fondos insuficientes")

# Verificar el saldo actual de la cuenta
print("Saldo actual:", cuenta.saldo)
