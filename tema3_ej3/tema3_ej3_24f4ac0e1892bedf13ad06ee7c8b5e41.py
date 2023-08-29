# completa el código de la función
class Cuenta:
  pass
 class Cuenta:

# pass

 def _init_(self,r,s):

  self.rut=r

  self.saldo=s

   

 def girar(self,giro):

  if self.saldo > giro:

   self.saldo=self.saldo-giro

   return True

  else:

   return False           