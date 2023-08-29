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

cuenta = Cuenta("12345678-9", 10000)


puede_girar = cuenta.girar(5000)
if puede_girar:
    print("Giro exitoso. Saldo actual:", cuenta.saldo)
else:
    print("No es posible realizar el giro. Saldo insuficiente.")
           