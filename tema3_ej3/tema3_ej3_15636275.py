class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,monto):
        if self.saldo>=monto:
            self.saldo=self.saldo-monto
            print("Nuevo monto: ", self.saldo)
            return True
        else:
            return False

    def __str__(self):
        return "Rut: " + self.rut + "  -  Saldo: " + str(self.saldo)