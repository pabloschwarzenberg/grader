 # completa el código de la función
class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,retirar):
        self.retirar=retirar

        self.saldo=self.saldo-retirar
        if self.saldo>0:
            return True
        else:
            return False