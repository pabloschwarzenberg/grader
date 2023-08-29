# completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        Cuenta.rut=rut
        Cuenta.saldo=saldo
    def girar(self,monto):
        saldo_restante= self.saldo - monto
        if(saldo_restante>0):
            self.saldo=saldo_restante
            u=True
        else:
            u=True
        return (u)
           