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
resultado = cuenta.girar(500)
if resultado:
    print("Giro realizado con éxito")
else:
    print("No se puede realizar el giro por fondos insuficientes")
