# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        Cuenta.rut=rut
        Cuenta.saldo=saldo

    def girar(self,monto):
        if monto>Cuenta.saldo:
            return False
        else:
            Cuenta.saldo=Cuenta.saldo-monto
            return True