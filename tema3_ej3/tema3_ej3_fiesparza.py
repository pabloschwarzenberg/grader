# completa el código de la función
class Cuenta:
  

  
  def _init_(self,rut,saldo):
       self.rut=" "
       self.saldo=0


  def setrut(self,rut):
      self.rut=rut

  def setsaldo(self,saldo):
      self.saldo=saldo


  def getrut(self):
      return self.rut

  def getsaldo(self):
      return self.saldo
       
  def _girar_(self,saldo):
     if self.saldo>0:
          
          return True
     else:
          return False


if __name__ == "__main__":

      p1=Cuenta(2,"w")
     

 