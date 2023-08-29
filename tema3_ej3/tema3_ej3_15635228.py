class Cuenta():
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo
         
    def setRut(self,rut):
        self.rut = rut
         
    def setSaldo(self,saldo):
        self.saldo = saldo
         
    def getRut(self):
        return self.rut
     
    def getSaldo(self):
        return self.saldo
 
    def girar(self,monto):
        if monto > self.getSaldo():
            return False
        else:
            self.setSaldo(self.getSaldo()-monto)
            return True
