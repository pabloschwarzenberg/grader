class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(self,monto):
        if self.saldo%2000 ==0:
            self.saldo= self.saldo - monto
            return True          
        else: 
            return False