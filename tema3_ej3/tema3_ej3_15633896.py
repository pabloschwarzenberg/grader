class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,n):
        if n<=self.saldo:
            self.saldo=self.saldo-n
            return True
        if n>self.saldo:
            return False
  
    def __str__(self):
        return self.rut+" "+self.saldo


           