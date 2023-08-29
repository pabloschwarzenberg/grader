# completa el código de la función
class Cuenta:
 def __init__(self,rut,saldo):
   self.rut=rut
   self.saldo=saldo
 def girar(self,giro):
     self.giro=giro
     if self.saldo-self.giro<0:
       return False
     else:
       self.saldo=self.saldo-giro
       return True

           