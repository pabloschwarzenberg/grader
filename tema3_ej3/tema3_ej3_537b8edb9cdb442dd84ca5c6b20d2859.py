class Cuenta:
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo
    def girar(self,giro):
        a=int(giro)
        b=int(self.saldo)
        if a<=b:
            self.saldo= b-a
            return True
        else:
            return False
            

           