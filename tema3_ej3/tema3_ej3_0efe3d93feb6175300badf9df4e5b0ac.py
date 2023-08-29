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
cuenta = CuentaCorriente("123456789-0", 50000)

monto_a_girar = 20000
if cuenta.girar(monto_a_girar):
    print(f"Giro exitoso de ${monto_a_girar}")
else:
    print("Saldo insuficiente")

monto_a_girar = 60000
if cuenta.girar(monto_a_girar):
    print(f"Giro exitoso de ${monto_a_girar}")
else:
    print("Saldo insuficiente")

print(f"Saldo actual: ${cuenta.saldo}")
