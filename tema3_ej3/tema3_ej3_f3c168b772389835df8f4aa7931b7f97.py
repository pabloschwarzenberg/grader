# completa el código de la función
class Cuenta:
  pass
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
cuenta = Cuenta("123456789", 1000)

puede_girar = cuenta.girar(500)
if puede_girar:
    print("Giro realizado con éxito")
else:
    print("Fondos insuficientes")

print("Saldo actual:", cuenta.saldo)
