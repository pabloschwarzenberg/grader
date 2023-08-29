# completa el código de la función
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

cuenta = CuentaCorriente("123456789", 1000)  # Crear una cuenta con rut "123456789" y saldo inicial de 1000

monto_giro = 500
puede_girar = cuenta.girar(monto_giro)  # Realizar un giro de 500

if puede_girar:
    print("Giro exitoso. Nuevo saldo:", cuenta.saldo)
else:
    print("Saldo insuficiente. No se pudo realizar el giro.")


     