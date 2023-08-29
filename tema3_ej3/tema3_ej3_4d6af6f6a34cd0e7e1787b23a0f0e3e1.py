class Cuenta:
    
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo        

    def girar(self,giro):
        if giro>self.saldo:
            return False
        
        else:
            self.saldo=self.saldo-giro
            return True
            
       
        

mipersona=Cuenta("19827759-2",10000)

if mipersona.girar(3000):
    print("Saldo:",mipersona.saldo)
else:
    print("No se puede girar")
           