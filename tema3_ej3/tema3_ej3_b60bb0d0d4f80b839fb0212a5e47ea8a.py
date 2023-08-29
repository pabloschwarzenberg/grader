class Cuenta:
    def __init__(self,rut,saldo):
        self.saldo=saldo
        self.rut=rut
    def girar(self,giro):
        self.giro=giro
        if int(self.saldo)>=int(self.giro):
            self.saldo=self.saldo-self.giro
            print("Nuevo saldo:",self.saldo)
            return True
        else:
            return False
        
    

           