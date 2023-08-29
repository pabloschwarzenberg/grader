class Cuenta:
 def __init__(self,Rut,saldo):
  self.rut=Rut
  self.saldo=saldo
 def girar(self,Cantidad):
  if Cantidad>self.saldo:
   return False
  else:
   self.saldo=self.saldo-Cantidad
   return True
           