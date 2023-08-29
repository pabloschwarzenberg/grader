# completa el código de la función
class Cuenta:
    def __init__(self):
        self.rut = ""
        self.saldo = 200000

    def girar(self):
        monto = int(input("Ingrese monto a girar: "))
        if monto > self.saldo:
            return False
        else:
            resultado = self.saldo - monto
            return True

a = Cuenta()
print(a.girar())
           