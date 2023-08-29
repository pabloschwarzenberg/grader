class Cuenta:
    def __init__(self,rut,saldo):
        self.rut=rut
        self.saldo=saldo
        
    def girar(self,giro):
        if self.saldo>=giro:
            self.saldo-=giro
            return True
        return False
        
if __name__=="__main__":
    rut=int(input("Ingrese rut: "))
    saldo=int(input("Ingrese saldo: "))
    cuenta1=Cuenta(rut,saldo) 
    giro=int(input("Ingrese giro: "))
    cuenta1.girar(giro)
    print(cuenta1.saldo)
    
