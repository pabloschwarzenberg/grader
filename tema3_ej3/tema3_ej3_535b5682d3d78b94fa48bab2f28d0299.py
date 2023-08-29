class Cuenta:
    def __init__(self,a,b):
        self.rut=a
        self.saldo=b
        pass
    def girar(self,giro):
        if self.saldo > giro:
            self.saldo=self.saldo-giro
            return True
        else:
            return False
    def __str__(self):
        return "RUT"+str(self.rut)+"###"+"saldo"+str(self.saldo)

r=Cuenta("1-9",10000)
print(r)
s=r.girar(5000)
print(s)
print(r)
           