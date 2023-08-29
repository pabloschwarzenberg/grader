# completa el código de la función
class Cuenta:
   def __init__(self,rut,saldo):
     self.rut = rut
     self.saldo = saldo
   def girar(self,cantidad):
     if cantidad <= self.saldo:
       self.saldo = self.saldo - cantidad
       return True
    
     else: 
       return False