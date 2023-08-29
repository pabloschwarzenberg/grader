class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
    def __str__(self):
        return self.rut+" "+str(self.saldo)
    def __sub__(self, other):
        resta=self.saldo-other
        return resta
    def __le__(self, other):
        if other<=self.saldo:
            return True
        else:
            return False
    def girar(self,other):
        if other<=self.saldo:
            self.saldo=self.saldo-other
            return self.saldo
        else:
            return False
