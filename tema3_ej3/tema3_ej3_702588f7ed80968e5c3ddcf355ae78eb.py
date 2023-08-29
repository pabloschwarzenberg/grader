# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut=rut
        self.saldo=saldo
    def girar(saldo,giro):
        giro=int(input("giro"))
        saldo=int(input("saldo"))
        if giro>saldo:
            return False
        else:
            saldo=saldo-giro
            return saldo and True
saldo=20000
giro=1000
c1=Cuenta(saldo,giro)
Cuenta.girar(saldo,giro)

            
  
           