class Cuenta:
    def __init__(self,rut=0,saldo=0):
        self.rut=rut
        self.saldo=saldo
    def girar(self,cantidad):
        if self.saldo>=cantidad:
            self.saldo=self.saldo-cantidad
            return True, self.saldo
        elif self.saldo<cantidad:
            return False
            
if __name__=="__main__":
    r=input("Ingrese rut: ")
    s=int(input("Ingrese saldo: "))
    cuenta=Cuenta(r,s)
    g=int(input("Ingrese monto de giro: "))
    k=cuenta.girar(g)
    print(k)
           