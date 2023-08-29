# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,monto):
        self.monto=monto
        if self.saldo>=monto:
            self.saldo=self.saldo-monto
            return True
        else:
            return False
cuenta=Cuenta("19.700.259-0",1200000)
print(cuenta.saldo)
print(cuenta.rut)
cuenta.girar(60000)
print(cuenta.saldo)


 
           