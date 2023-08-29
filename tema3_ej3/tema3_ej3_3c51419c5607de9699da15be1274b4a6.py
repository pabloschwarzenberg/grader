# completa el código de la función
class Cuenta:
 def __init__(self,RUT,saldo):
     self.RUT = RUT
     self.saldo = saldo
 def girar(self,monto):
     if self.saldo < monto:
         return False
     if self.saldo >= monto:
         self.saldo -= monto
         return True
           