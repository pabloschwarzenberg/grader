class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=int(saldo)
        
    def girar(self,monto):
        if monto>self.saldo:
            return(False)
        if monto<=self.saldo:
            self.saldo=self.saldo-monto
            print("En la cuenta le quedan",self.saldo, "pesos")
            return(True)
           