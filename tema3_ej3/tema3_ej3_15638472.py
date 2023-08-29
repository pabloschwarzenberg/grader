class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=""
        self.saldo=int(saldo)
    def setrut(self,rut):
        self.rut=rut
    def setsaldo(self,saldo):
        self.saldo=saldo
    def getrut(self):
        return self.rut
    def getsaldo(self):
        return self.saldo
    def __str__(self):
        return self.rut+";"+self.saldo
    def girar(self,a):
        if self.saldo>=a:
            self.saldo=self.saldo-a
            return True
        else:
            return False

           