# completa el código de la función
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

monto_a_girar = 500
if cuenta.girar(monto_a_girar):
    print("Giro exitoso")
    print("Nuevo saldo:", cuenta.saldo)
else:
    print("No es posible realizar el giro")

monto_a_girar = 1500
if cuenta.girar(monto_a_girar):
    print("Giro exitoso")
    print("Nuevo saldo:", cuenta.saldo)
else:
    print("No es posible realizar el giro")

           