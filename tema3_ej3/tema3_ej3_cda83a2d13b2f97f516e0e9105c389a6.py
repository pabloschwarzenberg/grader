class Cuenta :
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = int(saldo)
    def girar(self,monto):
        a = self.saldo
        if monto <= a :
            self.saldo = a - int(monto)
            return True
        else :
            return False

           