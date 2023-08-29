# completa el código de la función
class Cuenta:
  pass
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        else:
            return False
cuenta = Cuenta("123456789", 1000)  # Crear una cuenta con rut "123456789" y saldo de 1000
resultado = cuenta.girar(500)  # Intentar girar 500 desde la cuenta

if resultado:
    print("Giro exitoso")
else:
    print("Saldo insuficiente")
           