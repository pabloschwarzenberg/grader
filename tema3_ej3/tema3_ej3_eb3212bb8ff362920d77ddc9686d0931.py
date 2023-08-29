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
# Crear una instancia de la clase Cuenta
cuenta = Cuenta("123456789", 10000)

# Realizar un giro de 5000
if cuenta.girar(5000):
    print("Giro exitoso")
else:
    print("Fondos insuficientes")

# Verificar el saldo actual
print("Saldo actual:", cuenta.saldo)
