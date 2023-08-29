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
cuenta = CuentaCorriente("12345678-9", 10000)

monto_a_girar = 5000
if cuenta.girar(monto_a_girar):
    print(f"Se ha girado {monto_a_girar} pesos de la cuenta.")
    print(f"Saldo actual: {cuenta.saldo}")
else:
    print("No es posible realizar el giro. Saldo insuficiente.")