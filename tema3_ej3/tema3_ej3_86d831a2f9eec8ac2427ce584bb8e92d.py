class Cuenta:
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
cuenta = Cuenta("123456789", 1000)
print("Saldo inicial:", cuenta.saldo)
resultado = cuenta.girar(500)
if resultado:
    print("Giro exitoso. Nuevo saldo:", cuenta.saldo)
else:
    print("Fondos insuficientes. Saldo actual:", cuenta.saldo)
