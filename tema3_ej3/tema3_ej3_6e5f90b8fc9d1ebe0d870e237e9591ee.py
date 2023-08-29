class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo

    def girar(self,o):
        if o> self.saldo:
            return False
        elif self.saldo>=o:
            self.saldo+= -(o)
            return True
           